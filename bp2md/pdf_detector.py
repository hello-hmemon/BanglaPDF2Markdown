from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import fitz


@dataclass(slots=True)
class PDFInfo:
    pages: int
    has_text: bool
    tagged: bool
    encrypted: bool
    characters: int
    bangla_chars: int
    english_chars: int
    images: int
    corruption: float


class PDFDetector:

    def analyze(self, pdf: Path) -> PDFInfo:

        doc = fitz.open(pdf)

        text_parts: list[str] = []
        image_count = 0

        for page in doc:
            text_parts.append(page.get_text())
            image_count += len(page.get_images(full=True))

        text = "".join(text_parts)

        pages = len(doc)
        has_text = bool(text.strip())

        # PyMuPDF doesn't reliably expose Tagged PDF status.
        # Keep False for now. We'll improve later.
        tagged = False

        encrypted = doc.is_encrypted

        characters = len(text)

        bangla_chars = len(
            re.findall(r"[\u0980-\u09FF]", text)
        )

        english_chars = len(
            re.findall(r"[A-Za-z]", text)
        )

        replacement = text.count("\uFFFD")

        corruption = (
            replacement / max(characters, 1)
        ) * 100

        doc.close()

        return PDFInfo(
            pages=pages,
            has_text=has_text,
            tagged=tagged,
            encrypted=encrypted,
            characters=characters,
            bangla_chars=bangla_chars,
            english_chars=english_chars,
            images=image_count,
            corruption=corruption,
        )