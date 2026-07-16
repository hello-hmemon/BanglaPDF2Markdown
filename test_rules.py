from pathlib import Path

from bp2md.corpus import CorpusAnalyzer
from bp2md.rule_generator import RuleGenerator

folder = Path("output/pdfplumber")

counter = CorpusAnalyzer().analyze_folder(folder)

rules = RuleGenerator().generate(counter)

print()

print("Generated Rules")

print("=" * 40)

for rule in rules:

    print(f"{rule.pattern!r:<8}" f"{rule.frequency:>6}")
