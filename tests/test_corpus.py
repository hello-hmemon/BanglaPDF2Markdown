from tests.conftest import OUTPUT_DIR

from bp2md.corpus import CorpusAnalyzer

folder = OUTPUT_DIR / "pdfplumber"

counter = CorpusAnalyzer().analyze_folder(folder)

print()

print("Corpus Statistics")

print("=" * 40)

for pattern, count in counter.most_common():

    print(f"{pattern!r:<6} {count:>6}")
