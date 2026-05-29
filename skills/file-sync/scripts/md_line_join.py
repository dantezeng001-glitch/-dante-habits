"""Join broken lines in extracted Markdown files.

PDF text extraction often breaks sentences at the original column width,
producing short lines that should be continuous paragraphs. This script
detects and merges those broken lines while preserving intentional
line breaks (headings, lists, tables, blank lines, spec labels).

Usage:
  python md_line_join.py <file.md> [<file2.md> ...] [--in-place]

Without --in-place, prints cleaned content to stdout (single file) or
reports what would change (multiple files).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Known spec parameter names — lines matching exactly are never merged
# ---------------------------------------------------------------------------
SPEC_NAMES_LOWER: set[str] = {
    # English
    "part number", "model number", "speaker type", "frequency response",
    "speaker sensitivity", "sensitivity", "microphone sensitivity",
    "microphone", "bluetooth® version", "bluetooth version",
    "compatible profiles", "compatible configuration files",
    "charge voltage", "charging voltage", "maximum charge voltage",
    "frequency band", "wireless range", "speaker impedance",
    "battery", "battery capacity", "talk time", "continuous play",
    "listen time", "standby time", "charge time", "weight",
    "warranty", "water resistant", "water resistance",
    "sweat resistance", "sweat/water resistance",
    "maximum rf output power", "audio codecs supported",
    "quick charge", "materials", "chip", "charge type",
    "net weight", "gross weight", "bone conduction technology",
    # French
    "modèle", "couleur", "type de transducteur", "réponse en fréquence",
    "sensibilité du haut-parleur", "sensibilité du microphone",
    "version bluetooth", "profils compatibles", "tension de charge",
    "bande de fréquence", "portée sans fil", "batterie",
    "autonomie de lecture", "autonomie en veille", "temps de charge",
    "charge rapide", "poids", "garantie", "résistance à la sueur",
    "matériau extérieur", "codecs audio supportés",
    "capacité de la batterie", "poids brut", "poids net",
}

SECTION_HEADERS_UPPER: set[str] = {
    "SPECIFICATIONS", "SPEC", "CARACTÉRISTIQUES", "SPÉCIFICATIONS",
    "WHAT'S IN THE BOX", "WHAT\u2019S IN THE BOX",
    "CONTENU DE LA BOÎTE", "PACKAGING DIMENSIONS",
    "DIMENSION DE L'EMBALLAGE", "FEATURES", "COLOR", "COLORS",
}


def _strip_bold(s: str) -> str:
    return re.sub(r"\*\*", "", s).strip()


def _is_spec_name(line: str) -> bool:
    return _strip_bold(line).lower() in SPEC_NAMES_LOWER


def _is_section_header(line: str) -> bool:
    upper = _strip_bold(line).upper()
    return any(upper == h or upper.startswith(h) for h in SECTION_HEADERS_UPPER)


def join_broken_lines(text: str) -> str:
    """Merge PDF-broken sentences while preserving structural lines."""
    lines = text.split("\n")
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Never touch structural / label lines
        if (
            line.startswith("#")
            or line.startswith("|")
            or line.startswith("- ")
            or line.strip() == ""
            or line.startswith("```")
            or _is_spec_name(line.strip())
            or _is_section_header(line.strip())
        ):
            result.append(line)
            i += 1
            continue

        merged = line
        while i + 1 < len(lines):
            nxt_raw = lines[i + 1]
            nxt = nxt_raw.strip()
            if not nxt:
                break
            if (
                nxt_raw.startswith("#")
                or nxt_raw.startswith("|")
                or nxt_raw.startswith("- ")
                or nxt_raw.startswith("```")
            ):
                break
            if _is_spec_name(nxt) or _is_section_header(nxt):
                break

            cur = merged.rstrip()

            # Hyphenated word break: "com-\nplete" → "complete"
            if cur.endswith("-") and nxt and nxt[0].islower():
                if re.search(r"[a-zA-Z\u00C0-\u024F]-$", cur):
                    merged = cur[:-1] + nxt
                    i += 1
                    continue

            # Next line starts with lowercase → true sentence continuation
            if nxt and nxt[0].islower():
                sep = "" if cur.endswith(" ") else " "
                merged = cur + sep + nxt
                i += 1
                continue

            # Current line ends with comma → continuation regardless of case
            if cur.rstrip().endswith(",") and nxt:
                sep = "" if cur.endswith(" ") else " "
                merged = cur + sep + nxt
                i += 1
                continue

            break

        result.append(merged)
        i += 1

    return "\n".join(result)


# ---------------------------------------------------------------------------
# File-level helpers
# ---------------------------------------------------------------------------
def process_file(path: Path, *, in_place: bool = False) -> bool:
    """Join broken lines in a single MD file. Returns True if content changed."""
    content = path.read_text(encoding="utf-8")
    cleaned = join_broken_lines(content)

    if content == cleaned:
        return False

    if in_place:
        path.write_text(cleaned, encoding="utf-8")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Join broken lines in extracted Markdown files.",
    )
    parser.add_argument("files", nargs="+", type=Path, help="Markdown files to process")
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite files in place (default: dry-run report or stdout)",
    )
    args = parser.parse_args()

    if len(args.files) == 1 and not args.in_place:
        path = args.files[0]
        if not path.exists():
            print(f"Error: {path} not found", file=sys.stderr)
            sys.exit(1)
        content = path.read_text(encoding="utf-8")
        sys.stdout.write(join_broken_lines(content))
        return

    changed = 0
    for path in args.files:
        if not path.exists():
            print(f"  SKIP: {path} (not found)")
            continue
        if process_file(path, in_place=args.in_place):
            action = "Joined" if args.in_place else "Would join"
            print(f"  {action}: {path.name}")
            changed += 1
        else:
            print(f"  OK: {path.name}")

    verb = "Joined" if args.in_place else "Would join"
    print(f"\n{verb} broken lines in {changed}/{len(args.files)} file(s).")


if __name__ == "__main__":
    main()
