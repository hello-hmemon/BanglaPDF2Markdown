from tests.conftest import SAMPLE_PDF

from bp2md.pdf_detector import PDFDetector


def test_pdf_detector():

    detector = PDFDetector()

    info = detector.analyze(SAMPLE_PDF)

    assert info.pages > 0
    assert isinstance(info.has_text, bool)
    assert isinstance(info.tagged, bool)
    assert isinstance(info.encrypted, bool)

    assert info.characters > 0
    assert info.bangla_chars >= 0
    assert info.english_chars >= 0
    assert info.images >= 0
    assert info.corruption >= 0