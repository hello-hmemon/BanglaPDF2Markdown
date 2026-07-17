from pathlib import Path

from bp2md.repair_engine import BanglaRepairEngine

text = Path("output/pdfplumber/sample.txt").read_text(encoding="utf-8")

engine = BanglaRepairEngine()

result = engine.repair(text)

print()

print("Repair Report")

print("=" * 40)

print("Original :", result.original_score)

print("Repaired :", result.repaired_score)

print()

print("Rules")

for rule in result.applied_rules:

    print(" -", rule)

Path("output/repaired.txt").write_text(
    result.repaired_text,
    encoding="utf-8",
)

print()

print("Saved: output/repaired.txt")
