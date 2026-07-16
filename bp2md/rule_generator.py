from __future__ import annotations

from collections import Counter
from dataclasses import dataclass


@dataclass(slots=True)
class RepairRule:
    pattern: str
    frequency: int


class RuleGenerator:

    def generate(
        self,
        counter: Counter[str],
        minimum_frequency: int = 5,
    ) -> list[RepairRule]:

        rules: list[RepairRule] = []

        for pattern, count in counter.items():

            if count >= minimum_frequency:

                rules.append(
                    RepairRule(
                        pattern=pattern,
                        frequency=count,
                    )
                )

        rules.sort(
            key=lambda r: r.frequency,
            reverse=True,
        )

        return rules
