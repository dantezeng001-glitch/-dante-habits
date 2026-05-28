# -*- coding: utf-8 -*-
"""Compute weighted Shokz persona interest score from 1-5 persona scores.

Input modes:
  1. JSON string argument:  python weighted_score.py '{"scores": {...}}'
  2. File path argument:    python weighted_score.py scores.json
  3. Stdin:                 echo '{...}' | python weighted_score.py

Optional `weights.preset` selects one of the presets defined in
references/weight_presets.md. Default is the survey baseline.
"""

import json
import sys
from pathlib import Path


PERSONA_NAMES = ["科技老白男", "骨传导跑男", "日常颜值派", "日常开放派"]


PRESETS = {
    "default":   [0.218009, 0.315956, 0.162717, 0.303318],
    "costco":    [0.15, 0.20, 0.30, 0.35],
    "target":    [0.13, 0.20, 0.35, 0.32],
    "bos_dtc":   [0.25, 0.50, 0.05, 0.20],
    "seal_swim": [0.20, 0.35, 0.15, 0.30],
}


def load_payload():
    """Accept JSON string, file path, or stdin. Tolerate Windows non-ASCII paths and BOM."""
    if len(sys.argv) > 1:
        arg = sys.argv[1].lstrip("\ufeff")
        try:
            return json.loads(arg)
        except json.JSONDecodeError:
            return json.loads(Path(arg).read_text(encoding="utf-8-sig"))
    return json.loads(sys.stdin.read().lstrip("\ufeff"))


def resolve_weights(payload):
    """Return (weights_list, preset_label). Custom weights are normalized if sum within ±0.05."""
    weights_cfg = payload.get("weights", {})
    if isinstance(weights_cfg, list):
        custom = [float(w) for w in weights_cfg]
        return _normalize(custom), "custom"
    preset = weights_cfg.get("preset", "default") if isinstance(weights_cfg, dict) else "default"
    if preset == "custom":
        custom = weights_cfg.get("values")
        if not custom or len(custom) != 4:
            raise ValueError("custom preset requires 'values' list of 4 numbers")
        return _normalize([float(w) for w in custom]), "custom"
    if preset not in PRESETS:
        raise ValueError(f"unknown preset '{preset}'. Options: {list(PRESETS) + ['custom']}")
    return PRESETS[preset], preset


def _normalize(weights):
    total = sum(weights)
    if not 0.95 <= total <= 1.05:
        raise ValueError(f"custom weights must sum to 1.00 ± 0.05, got {total:.3f}")
    return [w / total for w in weights]


def get_score(scores, idx, name):
    candidates = [
        str(idx + 1),
        idx + 1,
        name,
        f"Persona {idx + 1}",
        f"persona_{idx + 1}",
        f"score_{idx + 1}",
        f"score_{name}",
    ]
    if name == "日常颜值派":
        candidates.extend(["设计通勤族", "score_设计通勤族"])
    for key in candidates:
        if key in scores:
            return float(scores[key])
    raise KeyError(f"Missing score for persona {idx + 1} {name}")


def main():
    payload = load_payload()
    scores = payload.get("scores", payload)
    weights, preset_label = resolve_weights(payload)

    rows = []
    weighted = 0.0
    for idx, (name, weight) in enumerate(zip(PERSONA_NAMES, weights)):
        score = get_score(scores, idx, name)
        if not 1 <= score <= 5:
            raise ValueError(f"Score for {name} must be between 1 and 5, got {score}")
        contribution = weight * score
        weighted += contribution
        rows.append({
            "id": str(idx + 1),
            "persona": name,
            "weight": round(weight, 6),
            "score_5": score,
            "weighted_contribution": round(contribution, 6),
        })

    result = {
        "preset": preset_label,
        "max_score": 5.0,
        "weighted_score_5": round(weighted, 4),
        "weighted_score_100": round(weighted / 5 * 100, 2),
        "personas": rows,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
