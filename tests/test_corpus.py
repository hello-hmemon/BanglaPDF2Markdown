from pathlib import Path

from bp2md.corpus import CorpusAnalyzer

folder = Path("output/pdfplumber")

counter = CorpusAnalyzer().analyze_folder(folder)

print()

print("Corpus Statistics")

print("=" * 40)

for pattern, count in counter.most_common():

    print(f"{pattern!r:<6} {count:>6}")
