from extractors.base import BaseExtractor
from extractors.markitdown_ext import MarkItDownExtractor
from extractors.pdfplumber_ext import PDFPlumberExtractor
from extractors.poppler_ext import PopplerExtractor
from extractors.pymupdf_ext import PyMuPDFExtractor


def get_extractors() -> list[BaseExtractor]:
    """
    Return all enabled extractors.

    Order matters.
    Best/fastest extractors should come first.
    """

    return [
        PyMuPDFExtractor(),
        PDFPlumberExtractor(),
        PopplerExtractor(),
        MarkItDownExtractor(),
    ]
