from __future__ import annotations

from pathlib import Path
from time import perf_counter

from bp2md.config import VERBOSE
from bp2md.csv_logger import CSVLogger
from bp2md.database import BenchmarkDatabase
from bp2md.output import OutputManager
from bp2md.quality import BanglaQualityScorer
from bp2md.repair_engine import BanglaRepairEngine
from extractors import get_extractors


class BenchmarkRunner:

    def __init__(self):

        self.extractors = get_extractors()
        self.scorer = BanglaQualityScorer()
        self.repair = BanglaRepairEngine()

        self.output = OutputManager()
        self.csv = CSVLogger()
        self.db = BenchmarkDatabase()

    def run(self, pdf: Path):

        results = []

        for extractor in self.extractors:

            if VERBOSE:
                print(f"\nRunning {extractor.name}...")

            start = perf_counter()

            result = extractor.extract(pdf)

            elapsed = perf_counter() - start

            if not result.success:

                print("✗ Failed")
                print(result.error)
                continue

            quality_before = self.scorer.score(
                result.text
            )

            repaired = self.repair.repair(
                result.text
            )

            final_text = repaired.repaired_text

            quality_after = self.scorer.score(
                final_text
            )

            output = self.output.save_text(
                extractor.name,
                pdf,
                final_text,
            )

            metadata = result.metadata

            pages = metadata.get(
                "pages",
                "?",
            )

            words = metadata.get(
                "words",
                0,
            )

            characters = metadata.get(
                "characters",
                len(final_text),
            )

            if VERBOSE:

                print("✓ Success")
                print(f"Time          : {elapsed:.3f} sec")
                print(f"Pages         : {pages}")
                print(f"Words         : {words:,}")
                print(f"Characters    : {characters:,}")

                print(
                    f"Score Before  : {quality_before.score}/100"
                )

                print(
                    f"Score After   : {quality_after.score}/100"
                )

                if repaired.applied_rules:

                    print("Repair Rules:")

                    for rule in repaired.applied_rules:
                        print(f"  - {rule}")

                print(f"Saved         : {output}")

            self.csv.append(
                pdf=pdf,
                extractor=extractor.name,
                score=quality_after.score,
                pages=pages,
                words=words,
                characters=characters,
            )

            self.db.insert(
                pdf=pdf,
                extractor=extractor.name,
                score=quality_after.score,
                pages=pages,
                words=words,
                characters=characters,
            )

            results.append(
                {
                    "extractor": extractor.name,
                    "score": quality_after.score,
                    "time": elapsed,
                    "output": output,
                    "text": final_text,
                }
            )

        self.save_winner(
            pdf,
            results,
        )

        self.db.close()

        return results

    def save_winner(
        self,
        pdf: Path,
        results: list[dict],
    ):

        if not results:

            print("\nNo successful extraction.")
            return

        results.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        winner = results[0]

        txt_file, md_file = self.output.save_final(
            pdf,
            winner["text"],
        )

        print("\n" + "=" * 60)
        print("Benchmark Summary")
        print("=" * 60)

        for i, item in enumerate(
            results,
            start=1,
        ):

            print(
                f"{i}. "
                f"{item['extractor']:<15}"
                f"{item['score']:>3}/100 "
                f"{item['time']:.3f}s"
            )

        print("-" * 60)

        print(
            f"Winner : {winner['extractor']}"
        )

        print(
            f"Score  : {winner['score']}/100"
        )

        print(
            f"Final TXT : {txt_file}"
        )

        print(
            f"Final MD  : {md_file}"
        )

        print("=" * 60)
