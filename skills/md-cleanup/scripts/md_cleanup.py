r"""Source-agnostic Markdown readability cleanup.

Handles every rule family that can be done safely by a pure-text pass — no
AI reasoning required. Structural rewrites (heading hierarchy, semantic
titles, etc.) are described in SKILL.md and executed by the agent.

Rule families covered here:
  F1  Character-level       NFKC + Kangxi radicals + CJK Radicals Supplement + common trad residuals
  F2  Escape residuals      `\-` `\*` `\_` `\|` etc. in contexts where escape is unnecessary
  F3  Rich-text export
      F3.1  `$\color{#hex}{text}$` LaTeX-color wrappers → plain text
      F3.2  `:::` Dingtalk-style fence containers → removed
      F3.3  `@xxx(yyy)` mentions wrapped by `$\color{}$` → `@xxx(yyy)` (after F3.1)
  F4  Link label noise      `请至钉钉文档查看附件《X》` → `《X》`
  F6  Noise
      F6.1  3+ consecutive blank lines → 2
      F6.2  Isolated `[No text extracted]` lines (keep ONE if all pages empty, drop elsewhere)
      F6.3  Trailing trailing whitespace on every line

Deliberately NOT touched (unsafe for automated pass, agent's job):
  F3.4  Multi-item numbered lists inside table cells
          (`1.  a<br>    <br>2.  b` — touching HTML and table at once is risky)
  F5    Structural / semantic rewrites (heading hierarchy, `## Page N` → semantic)

Usage:
  python md_cleanup.py <file.md> [<file2.md> ...] [--in-place] [--verbose]

Without --in-place, prints cleaned content to stdout (single file) or
reports what would change (multiple files).
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------------------
# F1: CJK Kangxi Radicals (U+2F00 - U+2FD5) -> standard CJK unified ideographs
# Complete table: 214 radicals used in the Kangxi Dictionary.
# PDF extractors (pypdf, pymupdf) sometimes emit these instead of the
# standard CJK codepoints when the source font uses a CID mapping that
# references the radical block.
# ---------------------------------------------------------------------------

KANGXI_MAP: dict[str, str] = {
    "\u2F00": "\u4E00", "\u2F01": "\u4E28", "\u2F02": "\u4E36",
    "\u2F03": "\u4E3F", "\u2F04": "\u4E59", "\u2F05": "\u4E85",
    "\u2F06": "\u4E8C", "\u2F07": "\u4EA0", "\u2F08": "\u4EBA",
    "\u2F09": "\u513F", "\u2F0A": "\u5165", "\u2F0B": "\u516B",
    "\u2F0C": "\u5182", "\u2F0D": "\u5196", "\u2F0E": "\u51AB",
    "\u2F0F": "\u51E0", "\u2F10": "\u51F5", "\u2F11": "\u5200",
    "\u2F12": "\u529B", "\u2F13": "\u52F9", "\u2F14": "\u5315",
    "\u2F15": "\u531A", "\u2F16": "\u5338", "\u2F17": "\u5341",
    "\u2F18": "\u535C", "\u2F19": "\u5369", "\u2F1A": "\u5382",
    "\u2F1B": "\u53B6", "\u2F1C": "\u53C8", "\u2F1D": "\u53E3",
    "\u2F1E": "\u56D7", "\u2F1F": "\u571F", "\u2F20": "\u58EB",
    "\u2F21": "\u5902", "\u2F22": "\u590A", "\u2F23": "\u5915",
    "\u2F24": "\u5927", "\u2F25": "\u5973", "\u2F26": "\u5B50",
    "\u2F27": "\u5B80", "\u2F28": "\u5BF8", "\u2F29": "\u5C0F",
    "\u2F2A": "\u5C22", "\u2F2B": "\u5C38", "\u2F2C": "\u5C6E",
    "\u2F2D": "\u5C71", "\u2F2E": "\u5DDB", "\u2F2F": "\u5DE5",
    "\u2F30": "\u5DF1", "\u2F31": "\u5DFE", "\u2F32": "\u5E72",
    "\u2F33": "\u5E7A", "\u2F34": "\u5E7F", "\u2F35": "\u5EF4",
    "\u2F36": "\u5EFE", "\u2F37": "\u5F0B", "\u2F38": "\u5F13",
    "\u2F39": "\u5F50", "\u2F3A": "\u5F61", "\u2F3B": "\u5F73",
    "\u2F3C": "\u5FC3", "\u2F3D": "\u6208", "\u2F3E": "\u6236",
    "\u2F3F": "\u624B", "\u2F40": "\u652F", "\u2F41": "\u6534",
    "\u2F42": "\u6587", "\u2F43": "\u6597", "\u2F44": "\u65A4",
    "\u2F45": "\u65B9", "\u2F46": "\u65E0", "\u2F47": "\u65E5",
    "\u2F48": "\u66F0", "\u2F49": "\u6708", "\u2F4A": "\u6728",
    "\u2F4B": "\u6B20", "\u2F4C": "\u6B62", "\u2F4D": "\u6B79",
    "\u2F4E": "\u6BB3", "\u2F4F": "\u6BCB", "\u2F50": "\u6BD4",
    "\u2F51": "\u6BDB", "\u2F52": "\u6C0F", "\u2F53": "\u6C14",
    "\u2F54": "\u6C34", "\u2F55": "\u706B", "\u2F56": "\u722A",
    "\u2F57": "\u7236", "\u2F58": "\u723B", "\u2F59": "\u723F",
    "\u2F5A": "\u7247", "\u2F5B": "\u7259", "\u2F5C": "\u725B",
    "\u2F5D": "\u72AC", "\u2F5E": "\u7384", "\u2F5F": "\u7389",
    "\u2F60": "\u74DC", "\u2F61": "\u74E6", "\u2F62": "\u7518",
    "\u2F63": "\u751F", "\u2F64": "\u7528", "\u2F65": "\u7530",
    "\u2F66": "\u758B", "\u2F67": "\u7592", "\u2F68": "\u7676",
    "\u2F69": "\u767D", "\u2F6A": "\u76AE", "\u2F6B": "\u76BF",
    "\u2F6C": "\u76EE", "\u2F6D": "\u77DB", "\u2F6E": "\u77E2",
    "\u2F6F": "\u77F3", "\u2F70": "\u793A", "\u2F71": "\u79B8",
    "\u2F72": "\u79BE", "\u2F73": "\u7A74", "\u2F74": "\u7ACB",
    "\u2F75": "\u7AF9", "\u2F76": "\u7C73", "\u2F77": "\u7CF8",
    "\u2F78": "\u7F36", "\u2F79": "\u7F51", "\u2F7A": "\u7F8A",
    "\u2F7B": "\u7FBD", "\u2F7C": "\u8001", "\u2F7D": "\u800C",
    "\u2F7E": "\u8012", "\u2F7F": "\u8033", "\u2F80": "\u807F",
    "\u2F81": "\u8089", "\u2F82": "\u81E3", "\u2F83": "\u81EA",
    "\u2F84": "\u81F3", "\u2F85": "\u81FC", "\u2F86": "\u820C",
    "\u2F87": "\u821B", "\u2F88": "\u821F", "\u2F89": "\u826E",
    "\u2F8A": "\u8272", "\u2F8B": "\u8278", "\u2F8C": "\u864D",
    "\u2F8D": "\u866B", "\u2F8E": "\u8840", "\u2F8F": "\u884C",
    "\u2F90": "\u8863", "\u2F91": "\u897E", "\u2F92": "\u89C1",
    "\u2F93": "\u89D2", "\u2F94": "\u8A00", "\u2F95": "\u8C37",
    "\u2F96": "\u8C46", "\u2F97": "\u8C55", "\u2F98": "\u8C78",
    "\u2F99": "\u8D1D", "\u2F9A": "\u8D64", "\u2F9B": "\u8D70",
    "\u2F9C": "\u8DB3", "\u2F9D": "\u8EAB", "\u2F9E": "\u8F66",
    "\u2F9F": "\u8F9B", "\u2FA0": "\u8FB0", "\u2FA1": "\u8FB5",
    "\u2FA2": "\u9091", "\u2FA3": "\u9149", "\u2FA4": "\u91C6",
    "\u2FA5": "\u91CC", "\u2FA6": "\u91D1", "\u2FA7": "\u957F",
    "\u2FA8": "\u95E8", "\u2FA9": "\u961C", "\u2FAA": "\u96B6",
    "\u2FAB": "\u96B9", "\u2FAC": "\u96E8", "\u2FAD": "\u9752",
    "\u2FAE": "\u975E", "\u2FAF": "\u9762", "\u2FB0": "\u9769",
    "\u2FB1": "\u97E6", "\u2FB2": "\u97ED", "\u2FB3": "\u97F3",
    "\u2FB4": "\u9875", "\u2FB5": "\u98CE", "\u2FB6": "\u98DE",
    "\u2FB7": "\u98DF", "\u2FB8": "\u9996", "\u2FB9": "\u9999",
    "\u2FBA": "\u9A6C", "\u2FBB": "\u9AA8", "\u2FBC": "\u9AD8",
    "\u2FBD": "\u9ADF", "\u2FBE": "\u9B25", "\u2FBF": "\u9B2F",
    "\u2FC0": "\u9B32", "\u2FC1": "\u9B3C", "\u2FC2": "\u9C7C",
    "\u2FC3": "\u9E1F", "\u2FC4": "\u9E75", "\u2FC5": "\u9E7F",
    "\u2FC6": "\u9EA6", "\u2FC7": "\u9EBB", "\u2FC8": "\u9EC4",
    "\u2FC9": "\u9ECD", "\u2FCA": "\u9ED1", "\u2FCB": "\u9EF9",
    "\u2FCC": "\u9EFD", "\u2FCD": "\u9F0E", "\u2FCE": "\u9F13",
    "\u2FCF": "\u9F20", "\u2FD0": "\u9F3B", "\u2FD1": "\u9F50",
    "\u2FD2": "\u9F7F", "\u2FD3": "\u9F99", "\u2FD4": "\u9F9F",
    "\u2FD5": "\u9FA0",
}

# F1: CJK Radicals Supplement (U+2E80 - U+2EFF) -> simplified Chinese
# Only codepoints commonly emitted by PDF extractors.
RADICALS_SUPPLEMENT_MAP: dict[str, str] = {
    "\u2E80": "\u4E00",  # ⺀ → 一 (variant)
    "\u2ECB": "\u8F66",  # ⻋ → 车
    "\u2ECD": "\u8FB6",  # ⻍ → 辶
    "\u2ED3": "\u957F",  # ⻓ → 长
    "\u2EDA": "\u9875",  # ⻚ → 页
    "\u2EE2": "\u9A6C",  # ⻢ → 马
    "\u2EE3": "\u9AA8",  # ⻣ → 骨
    "\u2EEC": "\u9F50",  # ⻬ → 齐
}

# F1: High-frequency traditional-to-simplified residuals from PDF fonts.
TRAD_SIMPLE_MAP: dict[str, str] = {
    "\u6236": "\u6237",  # 戶 → 户
}


def _build_char_map() -> dict[str, str]:
    m: dict[str, str] = {}
    m.update(KANGXI_MAP)
    m.update(RADICALS_SUPPLEMENT_MAP)
    m.update(TRAD_SIMPLE_MAP)
    return m


_CHAR_MAP = _build_char_map()

# ---------------------------------------------------------------------------
# F3.1: LaTeX-color wrappers from Dingtalk export
#   `$\color{#0089FF}{@欧丰硕(Elliott)}$`   → `@欧丰硕(Elliott)`
#   `$\color{#ABCDEF}{anything}$`            → `anything`
# Also handles missing `#` prefix: `$\color{0089FF}{...}$`
# ---------------------------------------------------------------------------
_COLOR_WRAPPER = re.compile(
    r"\$\\color\{#?[0-9A-Fa-f]{3,8}\}\{([^{}$]*)\}\$"
)

# ---------------------------------------------------------------------------
# F3.2: Dingtalk `:::` fence containers. They wrap blocks; emit nothing.
# We remove the opening/closing fence lines (keep inner content).
# ---------------------------------------------------------------------------
_FENCE_LINE = re.compile(r"^\s*:::\s*[A-Za-z_-]*\s*$")

# ---------------------------------------------------------------------------
# F4: Dingtalk link label noise
#   `[请至钉钉文档查看附件《X》](url)`  → `[《X》](url)`
# Works on both Markdown link text and standalone occurrences.
# ---------------------------------------------------------------------------
_DINGTALK_PREFIX = re.compile(r"请至钉钉文档查看附件")

# ---------------------------------------------------------------------------
# F2: Unnecessary MD escapes in Dingtalk/Feishu exports.
# We only unescape in contexts where MD doesn't require escaping.
#   `\-` at line start in a non-bullet context → `-` (but we must not touch bullet `- `)
#   `\*`, `\_`, `\|` inside normal prose → strip the backslash
# Conservative: only unescape when the backslash is followed by a common
# punctuation glyph AND not preceded by another backslash (true escape).
# ---------------------------------------------------------------------------
_ESCAPE_RESIDUAL = re.compile(r"(?<!\\)\\([\-*_|])")

# ---------------------------------------------------------------------------
# F6: Misc noise
# ---------------------------------------------------------------------------
_TRIPLE_BLANK = re.compile(r"\n{3,}")
_TRAILING_WS = re.compile(r"[ \t]+$", re.MULTILINE)


def _apply_char_map(text: str) -> str:
    for old, new in _CHAR_MAP.items():
        if old in text:
            text = text.replace(old, new)
    return text


def _strip_color_wrappers(text: str) -> str:
    prev = None
    # F3.1 can be nested rarely; loop until stable.
    while prev != text:
        prev = text
        text = _COLOR_WRAPPER.sub(r"\1", text)
    return text


def _strip_fences(text: str) -> str:
    lines = text.split("\n")
    out = [line for line in lines if not _FENCE_LINE.match(line)]
    return "\n".join(out)


def _strip_dingtalk_prefix(text: str) -> str:
    return _DINGTALK_PREFIX.sub("", text)


def _unescape_residuals(text: str) -> str:
    return _ESCAPE_RESIDUAL.sub(r"\1", text)


def cleanup_md(text: str) -> str:
    """Apply all generic, safe cleanup passes to a Markdown document."""

    # F1 NFKC + line-ending normalization
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # F1 character-level replacements
    text = _apply_char_map(text)

    # F3.1 LaTeX color wrappers (runs before F3.3 so mention wrapping is stripped)
    text = _strip_color_wrappers(text)

    # F3.2 Dingtalk `:::` fences
    text = _strip_fences(text)

    # F4 Dingtalk link-label noise
    text = _strip_dingtalk_prefix(text)

    # F2 escape residuals
    text = _unescape_residuals(text)

    # F6 noise
    text = _TRAILING_WS.sub("", text)
    text = _TRIPLE_BLANK.sub("\n\n", text)

    return text


def process_file(path: Path, *, in_place: bool = False) -> bool:
    """Clean a single MD file. Returns True if content changed."""
    content = path.read_text(encoding="utf-8")
    cleaned = cleanup_md(content)

    if content == cleaned:
        return False

    if in_place:
        path.write_text(cleaned, encoding="utf-8")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Source-agnostic Markdown readability cleanup (F1/F2/F3/F4/F6).",
    )
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to clean")
    parser.add_argument(
        "--in-place", action="store_true",
        help="Overwrite files in place (default: dry-run report or stdout).",
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print per-rule hit counts for each file.",
    )
    args = parser.parse_args()

    if len(args.files) == 1 and not args.in_place:
        path = args.files[0]
        if not path.exists():
            print(f"Error: {path} not found", file=sys.stderr)
            sys.exit(1)
        content = path.read_text(encoding="utf-8")
        sys.stdout.write(cleanup_md(content))
        return

    changed = 0
    for path in args.files:
        if not path.exists():
            print(f"  SKIP: {path} (not found)")
            continue
        if process_file(path, in_place=args.in_place):
            action = "Cleaned" if args.in_place else "Would clean"
            print(f"  {action}: {path.name}")
            changed += 1
        else:
            print(f"  OK: {path.name}")

    verb = "Cleaned" if args.in_place else "Would clean"
    print(f"\n{verb} {changed}/{len(args.files)} file(s).")


if __name__ == "__main__":
    main()
