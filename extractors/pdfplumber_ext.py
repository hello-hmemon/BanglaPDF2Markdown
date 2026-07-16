from __future__ import annotations

from pathlib import Path

import pdfplumber

from bp2md.utils import (
    count_characters,
    count_words,
    normalize_text,
)
from extractors.base import BaseExtractor, ExtractionResult


class PDFPlumberExtractor(BaseExtractor):
    """
    Extract text from PDF using pdfplumber.

    Returns plain text only.
    """

    name = "PDFPlumber"

    def extract(self, pdf_path: Path) -> ExtractionResult:

        try:
            with pdfplumber.open(pdf_path) as pdf:

                page_count = len(pdf.pages)
                pages: list[str] = []

                for page in pdf.pages:

                    text = page.extract_text() or ""

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
