from __future__ import annotations

from collections import Counter
from pathlib import Path

from bp2md.bangla_repair import BanglaRepairAnalyzer


class CorpusAnalyzer:

    def analyze_folder(self, folder: Path) -> Counter[str]:

        analyzer = BanglaRepairAnalyzer()

        counter: Counter[str] = Counter()

        for file in folder.glob("*.txt"):

            text = file.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            for item in analyzer.analyze(text):
                counter[item.pattern] += item.occurrences

        return counter
