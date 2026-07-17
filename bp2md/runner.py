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

            repair = self.repair.repair(result.text)

            output = self.output.save_text(
                extractor.name,
                pdf,
                repair.repaired_text,
            )

            metadata = result.metadata

            pages = metadata.get("pages", "?")
            words = metadata.get("words", 0)
            characters = metadata.get(
                "characters",
                len(repair.repaired_text),
            )

            if VERBOSE:

                print("✓ Success")
                print(f"Time          : {elapsed:.3f} sec")
                print(f"Pages         : {pages}")
                print(f"Words         : {words:,}")
                print(f"Characters    : {characters:,}")
                print(f"Score Before  : {repair.original_score}/100")
                print(f"Score After   : {repair.repaired_score}/100")

                if repair.applied_rules:
                    print("Repair Rules:")
                    for rule in repair.applied_rules:
                        print(f"  - {rule}")

                print(f"Saved         : {output}")

            self.csv.append(
                pdf=pdf,
                extractor=extractor.name,
                score=repair.repaired_score,
                pages=pages,
                words=words,
                characters=characters,
            )

            self.db.insert(
                pdf=pdf,
                extractor=extractor.name,
                score=repair.repaired_score,
                pages=pages,
                words=words,
                characters=characters,
            )

            results.append(
                {
                    "extractor": extractor.name,
                    "score": repair.repaired_score,
                    "time": elapsed,
                    "characters": characters,
                    "pages": pages,
                    "words": words,
                    "output": output,
                    "text": repair.repaired_text,
                }
            )

        self.print_summary(pdf, results)

        self.db.close()

        return results

    def print_summary(self, pdf: Path, results):

        if not results:
            print("\nNo successful extraction.")
            return

        results.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        benchmark_winner = results[0]

        final_result = benchmark_winner

        for r in results:
            if r["extractor"].lower() == "poppler":
                final_result = r
                break

        txt_file, md_file = self.output.save_final(
            pdf,
            final_result["text"],
        )

        print("\n" + "=" * 60)
        print("Benchmark Summary")
        print("=" * 60)

        for i, r in enumerate(results, start=1):
            print(
                f"{i}. "
                f"{r['extractor']:<15}"
                f"{r['score']:>3}/100  "
                f"{r['time']:.3f}s"
            )

        print("-" * 60)
        print(
            f"Benchmark Winner : "
            f"{benchmark_winner['extractor']} "
            f"({benchmark_winner['score']}/100)"
        )

        if final_result["extractor"] == benchmark_winner["extractor"]:
            print(f"Final Output     : {final_result['extractor']}")
        else:
            print(
                f"Final Output     : {final_result['extractor']} "
                f"(layout preference)"
            )

        print(f"Final TXT        : {txt_file}")
        print(f"Final MD         : {md_file}")
        print("=" * 60)