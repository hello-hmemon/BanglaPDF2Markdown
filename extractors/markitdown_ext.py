from __future__ import annotations

from pathlib import Path

from markitdown import MarkItDown

from bp2md.utils import (
    count_characters,
    count_words,
    normalize_text,
)
from extractors.base import BaseExtractor, ExtractionResult


class MarkItDownExtractor(BaseExtractor):
    """
    Extract text using Microsoft MarkItDown.
    """

    name = "MarkItDown"

    def __init__(self):
        self.md = MarkItDown()

    def extract(self, pdf_path: Path) -> ExtractionResult:

        try:

            result = self.md.convert(str(pdf_path))

            text = normalize_text(result.text_content)

            return ExtractionResult(
                extractor=self.name,
                text=text,
                success=True,
                metadata={
                    "characters": count_characters(text),
                    "words": count_words(text),
                },
            )

        except Exception as e:

            return ExtractionResult(
                extractor=self.name,
                text="",
                success=False,
                error=str(e),
            )
