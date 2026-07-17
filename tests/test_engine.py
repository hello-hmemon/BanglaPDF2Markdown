from tests.conftest import REPAIRED_TXT, SAMPLE_TXT

from bp2md.repair_engine import BanglaRepairEngine


def test_repair_engine_improves_or_keeps_score():

    text = SAMPLE_TXT.read_text(encoding="utf-8")

    engine = BanglaRepairEngine()

    result = engine.repair(text)

    # Basic checks
    assert result.original_score >= 0
    assert result.repaired_score >= result.original_score
    assert result.repaired_text.strip() != ""

    # Save repaired output for manual inspection
    REPAIRED_TXT.write_text(
        result.repaired_text,
        encoding="utf-8",
    )