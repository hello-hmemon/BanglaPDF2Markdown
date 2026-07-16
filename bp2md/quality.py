from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(slots=True)
class QualityResult:
    score: int
    issues: list[str]

    replacement_count: int
    bangla_count: int
    english_count: int
    corruption_ratio: float


class BanglaQualityScorer:

    IMPOSSIBLE_SEQUENCES = (
        "াি",
        "েি",
        "োি",
        "ৌি",
        "্্",
        "।।",
    )

    def score(self, text: str) -> QualityResult:

        if not text.strip():
            return QualityResult(
                score=0,
                issues=["Empty output"],
                replacement_count=0,
                bangla_count=0,
                english_count=0,
                corruption_ratio=1.0,
            )

        score = 100
        issues: list[str] = []

        replacement = text.count("\ufffd")

        bangla = len(re.findall(r"[\u0980-\u09FF]", text))
        english = len(re.findall(r"[A-Za-z]", text))

        corruption_ratio = replacement / bangla if bangla else 0.0

        if replacement:
            penalty = min(replacement * 5, 30)
            score -= penalty
            issues.append(f"Replacement characters: {replacement}")

        if bangla > 200:

            ratio = english / bangla

            if ratio > 0.60:
                score -= 10
                issues.append("Too much English text")

        for seq in self.IMPOSSIBLE_SEQUENCES:

            n = text.count(seq)

            if n:
                score -= min(n * 2, 20)
                issues.append(f"'{seq}' x {n}")

        multi_spaces = len(re.findall(r" {3,}", text))

        if multi_spaces:
            score -= min(multi_spaces, 5)

        score = max(score, 0)

        return QualityResult(
            score=score,
            issues=issues,
            replacement_count=replacement,
            bangla_count=bangla,
            english_count=english,
            corruption_ratio=corruption_ratio,
        )
