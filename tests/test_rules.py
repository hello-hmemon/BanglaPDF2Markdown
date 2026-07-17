from tests.conftest import OUTPUT_DIR

from bp2md.corpus import CorpusAnalyzer
from bp2md.rule_generator import RuleGenerator


def test_rule_generator():

    folder = OUTPUT_DIR / "pdfplumber"

    counter = CorpusAnalyzer().analyze_folder(folder)

    rules = RuleGenerator().generate(counter)

    # Should return a list
    assert isinstance(rules, list)

    # Every generated rule should be valid
    for rule in rules:
        assert rule.pattern
        assert rule.frequency >= 0