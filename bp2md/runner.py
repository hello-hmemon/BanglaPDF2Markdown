from __future__ import annotations

from pathlib import Path

from bp2md.config import VERBOSE
from bp2md.output import OutputManager
from bp2md.quality import BanglaQualityScorer
from extractors import get_extractors
from bp2md.csv_logger import CSVLogger
from bp2md.database import BenchmarkDatabase


class BenchmarkRunner:

    def __init__(self):
        self.extractors = get_extractors()
        self.scorer = BanglaQualityScorer()
        self.output = OutputManager()
        self.csv = CSVLogger()
        self.db = BenchmarkDatabase()

    def run(self, pdf: Path):

        results = []

        for extractor in self.extractors:

            if VERBOSE:
                print(f"\nRunning {extractor.name}...")

            result = extractor.extract(pdf)

            if not result.success:
                print("✗ Failed")
                print(result.error)
                continue

            output = self.output.save_text(
                extractor.name,
                pdf,
                result.text,
            )

            quality = self.scorer.score(result.text)

            metadata = result.metadata

            pages = metadata.get("pages", "?")
            words = metadata.get("words", 0)
            characters = metadata.get(
                "characters",
                len(result.text),
            )

            if VERBOSE:

                print("✓ Success")
                print(f"Pages      : {pages}")
                print(f"Words      : {words:,}")
                print(f"Characters : {characters:,}")
                print(f"Score      : {quality.score}/100")
                print(f"Bangla     : {quality.bangla_count:,}")
                print(f"Replacement: {quality.replacement_count:,}")

                if quality.issues:
                    print("Issues:")
                    for issue in quality.issues:
                        print(f"  - {issue}")

                print(f"Saved      : {output}")

            self.csv.append(
                pdf=pdf,
                extractor=extractor.name,
                score=quality.score,
                pages=pages,
                words=words,
                characters=characters,
            )

            self.db.insert(
                pdf=pdf,
                extractor=extractor.name,
                score=quality.score,
                pages=pages,
                words=words,
                characters=characters,
            )

            results.append(
                {
                    "extractor": extractor.name,
                    "score": quality.score,
                    "pages": pages,
                    "words": words,
                    "characters": characters,
                    "output": output,
                }
            )

        self.print_summary(results)

        self.db.close()

        return results

    def print_summary(self, results):

        if not results:
            print("\nNo successful extraction.")
            return

        results.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        print("\n" + "=" * 50)
        print("Benchmark Summary")
        print("=" * 50)

        for i, r in enumerate(results, 1):
            print(f"{i:>2}. " f"{r['extractor']:<15} " f"{r['score']:>3}/100")

        winner = results[0]

        print("-" * 50)
        print(f"Winner : {winner['extractor']}")
        print(f"Score  : {winner['score']}/100")
        print(f"Output : {winner['output']}")
        print("=" * 50)
