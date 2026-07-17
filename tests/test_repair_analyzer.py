from tests.conftest import SAMPLE_TXT

from bp2md.bangla_repair import BanglaRepairAnalyzer

text = SAMPLE_TXT.read_text(encoding="utf-8")

analyzer = BanglaRepairAnalyzer()

items = analyzer.analyze(text)

print()

print("Bangla Repair Analysis")

print("=" * 40)

for item in items:

    print(f"{item.pattern!r:<6} " f"{item.occurrences:>5}  " f"{item.description}")
