from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import fitz  # PyMuPDF

from bp2md.utils import (
    count_bangla_characters,
    count_characters,
)


@dataclass(slots=True)
class PDFAnalysis:

    file: str

    pages: int

    has_text: bool

    tagged: bool

    characters: int

    bangla_characters: int

    replacement_count: int

    corruption_ratio: float

    ocr_recommended: bool


class PDFDetector:

    def analyze(self, pdf_path: Path) -> PDFAnalysis:

        with fitz.open(pdf_path) as doc:

            pages = len(doc)

            metadata = doc.metadata

            tagged = False

            # PyMuPDF metadata সবসময় Tagged দেয় না,
            # তাই আপাতত False থাকবে
            if metadata:
                tagged = metadata.get("tagged", False)

            text_parts = []

            for page in doc:
                text_parts.append(page.get_text("text"))

            text = "\n".join(text_parts)

            characters = count_characters(text)

            bangla_chars = count_bangla_characters(text)

            replacement_count = text.count("\ufffd")

            if characters > 0:

                corruption_ratio = replacement_count / characters

            else:
                corruption_ratio = 0

            has_text = characters > 20

            # Decision rule
            ocr_recommended = not has_text or corruption_ratio > 0.05

            return PDFAnalysis(
                file=str(pdf_path),
                pages=pages,
                has_text=has_text,
                tagged=tagged,
                characters=characters,
                bangla_characters=bangla_chars,
                replacement_count=replacement_count,
                corruption_ratio=corruption_ratio,
                ocr_recommended=ocr_recommended,
            )
