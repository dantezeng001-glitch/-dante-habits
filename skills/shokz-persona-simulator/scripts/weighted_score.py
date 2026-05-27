# -*- coding: utf-8 -*-
"""Compute weighted Shokz persona interest score from 1-5 persona scores."""

import json
import sys
from pathlib import Path


PERSONAS = [
    {"id": "1", "name": "科技老白男", "weight": 0.218009},
    {"id": "2", "name": "骨传导跑男", "weight": 0.315956},
    {"id": "3", "name": "日常颜值派", "weight": 0.162717},
    {"id": "4", "name": "日常开放派", "weight": 0.303318},
]


def load_payload():
    if len(sys.argv) > 1:
        return json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    return json.loads(sys.stdin.read())


def get_score(scores, persona):
    keys = [
        persona["id"],
        int(persona["id"]),
        persona["name"],
        f"Persona {persona['id']}",
        f"persona_{persona['id']}",
        f"score_{persona['id']}",
        f"score_{persona['name']}",
    ]
    if persona["id"] == "3":
        keys.extend(["设计通勤族", "score_设计通勤族"])
    for key in keys:
        if key in scores:
            return float(scores[key])
    raise KeyError(f"Missing score for persona {persona['id']} {persona['name']}")


def main():
    payload = load_payload()
    scores = payload.get("scores", payload)
    rows = []
    weighted = 0.0
    for persona in PERSONAS:
        score = get_score(scores, persona)
        if not 1 <= score <= 5:
            raise ValueError(f"Score for {persona['name']} must be between 1 and 5, got {score}")
        contribution = persona["weight"] * score
        weighted += contribution
        rows.append({
            "id": persona["id"],
            "persona": persona["name"],
            "weight": persona["weight"],
            "score_5": score,
            "weighted_contribution": contribution,
        })
    result = {
        "max_score": 5.0,
        "weighted_score_5": round(weighted, 4),
        "weighted_score_100": round(weighted / 5 * 100, 2),
        "personas": rows,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
