from __future__ import annotations

from pathlib import Path

import fitz  # PyMuPDF

from bp2md.utils import (
    count_characters,
    count_words,
    normalize_text,
)
from extractors.base import BaseExtractor, ExtractionResult


class PyMuPDFExtractor(BaseExtractor):
    """
    Extract text from PDF using PyMuPDF.

    Returns plain text only.
    """

    name = "PyMuPDF"

    def extract(self, pdf_path: Path) -> ExtractionResult:

        try:
            with fitz.open(pdf_path) as doc:

                page_count = len(doc)
                pages: list[str] = []

                for page in doc:
                    text = page.get_text("text")

                    pages.append(normalize_text(text))

                full_text = "\n\n".join(pages).strip()

                return ExtractionResult(
                    extractor=self.name,
                    text=full_text,
                    success=True,
                    metadata={
                        "pages": page_count,
                        "characters": count_characters(full_text),
                        "words": count_words(full_text),
                    },
                )

        except Exception as e:
            return ExtractionResult(
                extractor=self.name,
                text="",
                success=False,
                error=str(e),
            )
