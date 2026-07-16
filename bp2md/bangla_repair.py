from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RepairSuggestion:
    pattern: str
    occurrences: int
    description: str


class BanglaRepairAnalyzer:

    COMMON_PATTERNS = {
        "াি": "Wrong vowel sign order",
        "েি": "Wrong vowel sign order",
        "োি": "Wrong vowel sign order",
        "ৌি": "Wrong vowel sign order",
        "াা": "Duplicated AA-kar",
        "েে": "Duplicated E-kar",
        "িি": "Duplicated I-kar",
        "ীী": "Duplicated II-kar",
        "ুু": "Duplicated U-kar",
        "ূূ": "Duplicated UU-kar",
        "্্": "Duplicated Hasanta",
        "।।": "Duplicated Danda",
    }

    def analyze(self, text: str) -> list[RepairSuggestion]:

        suggestions: list[RepairSuggestion] = []

        for pattern, description in self.COMMON_PATTERNS.items():

            count = text.count(pattern)

            if count:

                suggestions.append(
                    RepairSuggestion(
                        pattern=pattern,
                        occurrences=count,
                        description=description,
                    )
                )

        suggestions.sort(
            key=lambda x: x.occurrences,
            reverse=True,
        )

        return suggestions
