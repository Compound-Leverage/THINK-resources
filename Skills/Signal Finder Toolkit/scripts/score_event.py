#!/usr/bin/env python3
"""
score_event.py — Deterministic capital-event scorer for the Signal Finder Toolkit.

Mirrors the canonical scoring system defined in the capital-event-radar skill so
that Phase 2 scores are consistent across every run and every CL surface.

DO NOT READ THIS FILE INTO CONTEXT TO SCORE BY HAND. Run it and use the output.

Usage:
  python3 score_event.py '{"funding": 2500000, "timeline": "pre-rfp",
      "competition": "unsolicited", "geography": "target",
      "bonuses": ["multi-year"], "penalties": []}'

  # or named flags:
  python3 score_event.py --funding 300000 --timeline 3-6mo \
      --competition open --geography target

Canonical rubric (capital-event-radar):
  Funding Size  (40): $1M+=40, $250K-$1M=30, $50-249K=20, <$50K=10
  Timeline      (20): pre-rfp/planning=20, 6-12mo=15, 3-6mo=10, <3mo=5
  Competition   (20): unsolicited/sole-source=20, limited=15, set-aside=10, open=5
  Geography     (20): target(DE/MD/PA/VA/DC)=20, federal-local=15, adjacent=10, out-of-region=0
  Bonus  +10: unsolicited / multi-year / planning-grant
  Bonus   +5: partnership-required / regional / intermediary-eligible / pre-proposal-conference
  Penalty -5: single-state(non-target) / previous-awardee-preference / faith-based-or-tribal-only
  Score is clamped to 0-100.

Routing tiers (canonical cutoffs) and Signal Finder lead-magnet labels:
  85-100 -> 🔴 Synthesize Now   -> "MOVE NOW"
  70-84  -> 🟡 Synthesize Week  -> "MOVE THIS MONTH"
  50-69  -> 🟢 Nurture          -> "WATCH"
  <50    -> ⚪ Monitor          -> "MONITOR"
"""

import argparse
import json
import sys


def _norm(s):
    return str(s).strip().lower().replace("_", "-").replace(" ", "-")


def score_funding(amount):
    try:
        a = float(amount)
    except (TypeError, ValueError):
        return 10
    if a >= 1_000_000:
        return 40
    if a >= 250_000:
        return 30
    if a >= 50_000:
        return 20
    return 10


TIMELINE = {
    "pre-rfp": 20, "prerfp": 20, "planning": 20, "planning-grant": 20,
    "6-12mo": 15, "6-12": 15, "6to12mo": 15,
    "3-6mo": 10, "3-6": 10,
    "<3mo": 5, "lt3mo": 5, "under-3mo": 5, "3mo": 5,
}

COMPETITION = {
    "unsolicited": 20, "sole-source": 20, "sole": 20,
    "limited": 15,
    "set-aside": 10, "setaside": 10,
    "open": 5,
}

GEOGRAPHY = {
    "target": 20,
    "federal-local": 15, "federal-w-local-delivery": 15, "federal": 15,
    "adjacent": 10,
    "out-of-region": 0, "out": 0, "national": 0,
}

BONUS_10 = {"unsolicited", "multi-year", "multiyear", "planning-grant", "planning"}
BONUS_5 = {"partnership-required", "partnership", "regional", "regional-approach",
           "intermediary-eligible", "intermediary", "pre-proposal-conference",
           "pre-proposal"}
PENALTY = {"single-state", "single-state-non-target", "previous-awardee-preference",
           "previous-awardee", "faith-based-only", "tribal-only",
           "faith-based-or-tribal-only"}


def _lookup(table, value, factor):
    key = _norm(value)
    if key not in table:
        raise SystemExit(
            f"ERROR: unrecognized {factor} value '{value}'. "
            f"Valid: {', '.join(sorted(set(table)))}"
        )
    return table[key]


def score(event):
    funding = score_funding(event.get("funding", 0))
    timeline = _lookup(TIMELINE, event.get("timeline", "<3mo"), "timeline")
    competition = _lookup(COMPETITION, event.get("competition", "open"), "competition")
    geography = _lookup(GEOGRAPHY, event.get("geography", "out-of-region"), "geography")

    flags = {_norm(b) for b in event.get("bonuses", [])}
    pen_flags = {_norm(p) for p in event.get("penalties", [])}

    bonus = (10 if flags & BONUS_10 else 0) + (5 if flags & BONUS_5 else 0)
    penalty = -5 if pen_flags & PENALTY else 0

    raw = funding + timeline + competition + geography + bonus + penalty
    total = max(0, min(100, raw))

    if total >= 85:
        tier, label = "🔴 Synthesize Now", "MOVE NOW"
    elif total >= 70:
        tier, label = "🟡 Synthesize This Week", "MOVE THIS MONTH"
    elif total >= 50:
        tier, label = "🟢 Nurture", "WATCH"
    else:
        tier, label = "⚪ Monitor", "MONITOR"

    return {
        "score": total,
        "tier": tier,
        "label": label,
        "breakdown": {
            "funding": funding,
            "timeline": timeline,
            "competition": competition,
            "geography": geography,
            "bonus": bonus,
            "penalty": penalty,
        },
    }


def main():
    if len(sys.argv) == 2 and sys.argv[1].lstrip().startswith("{"):
        event = json.loads(sys.argv[1])
    else:
        p = argparse.ArgumentParser(description="Score a capital event (0-100).")
        p.add_argument("--funding", default=0, help="Funding amount in dollars")
        p.add_argument("--timeline", default="<3mo")
        p.add_argument("--competition", default="open")
        p.add_argument("--geography", default="out-of-region")
        p.add_argument("--bonuses", default="", help="Comma-separated bonus flags")
        p.add_argument("--penalties", default="", help="Comma-separated penalty flags")
        a = p.parse_args()
        event = {
            "funding": a.funding,
            "timeline": a.timeline,
            "competition": a.competition,
            "geography": a.geography,
            "bonuses": [x for x in a.bonuses.split(",") if x.strip()],
            "penalties": [x for x in a.penalties.split(",") if x.strip()],
        }

    result = score(event)
    b = result["breakdown"]
    print(f"SCORE: {result['score']}/100  ->  {result['tier']}  ({result['label']})")
    print(
        f"  Funding {b['funding']} | Timeline {b['timeline']} | "
        f"Competition {b['competition']} | Geography {b['geography']} | "
        f"Bonus {b['bonus']} | Penalty {b['penalty']}"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
