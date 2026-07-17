from tests.conftest import SAMPLE_TXT

from bp2md.bangla_repair import BanglaRepairAnalyzer


def test_repair_analyzer():

    text = SAMPLE_TXT.read_text(encoding="utf-8")

    analyzer = BanglaRepairAnalyzer()

    items = analyzer.analyze(text)

    # Should return a list
    assert isinstance(items, list)

    # Every item should have valid data
    for item in items:
        assert item.pattern
        assert item.description
        assert item.occurrences >= 0