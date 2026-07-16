from __future__ import annotations

import csv
from pathlib import Path

from bp2md.config import OUTPUT_DIR


class CSVLogger:

    def __init__(self):

        self.csv_file = OUTPUT_DIR / "benchmark.csv"

        self.csv_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.csv_file.exists():

            with self.csv_file.open(
                "w",
                newline="",
                encoding="utf-8",
            ) as f:

                writer = csv.writer(f)

                writer.writerow(
                    [
                        "PDF",
                        "Extractor",
                        "Score",
                        "Pages",
                        "Words",
                        "Characters",
                    ]
                )

    def append(
        self,
        pdf,
        extractor,
        score,
        pages,
        words,
        characters,
    ):

        with self.csv_file.open(
            "a",
            newline="",
            encoding="utf-8",
        ) as f:

            writer = csv.writer(f)

            writer.writerow(
                [
                    pdf.name,
                    extractor,
                    score,
                    pages,
                    words,
                    characters,
                ]
            )