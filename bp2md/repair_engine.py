from __future__ import annotations

from dataclasses import dataclass

from bp2md.quality import BanglaQualityScorer


@dataclass(slots=True)
class RepairResult:
    original_score: int
    repaired_score: int

    original_text: str
    repaired_text: str

    applied_rules: list[str]


class BanglaRepairEngine:

    RULES = [
        ("াি", "ি"),
        ("েি", "ি"),
        ("োি", "ি"),
        ("ৌি", "ি"),
        ("।।", "।"),
        ("্্", "্"),
    ]

    def repair(self, text: str) -> RepairResult:

        scorer = BanglaQualityScorer()

        before = scorer.score(text)

        repaired = text

        applied: list[str] = []

        for old, new in self.RULES:

            if old not in repaired:
                continue

            candidate = repaired.replace(old, new)

            candidate_score = scorer.score(candidate)

            if candidate_score.score >= before.score:

                repaired = candidate

                before = candidate_score

                applied.append(f"{old} → {new}")

        return RepairResult(
            original_score=scorer.score(text).score,
            repaired_score=before.score,
            original_text=text,
            repaired_text=repaired,
            applied_rules=applied,
        )
