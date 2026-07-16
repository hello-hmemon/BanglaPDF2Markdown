from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import fitz


@dataclass(slots=True)
class PDFInfo:
    pages: int
    has_text: bool
    tagged: bool
    characters: int


class PDFDetector:

    def analyze(self, pdf: Path) -> PDFInfo:

        doc = fitz.open(pdf)

        text = ""
        tagged = False

        try:
            metadata = doc.metadata or {}
            tagged = metadata.get("tagged", False)
        except Exception:
            pass

        for page in doc:
            text += page.get_text()

        info = PDFInfo(
            pages=len(doc),
            has_text=bool(text.strip()),
            tagged=tagged,
            characters=len(text),
        )

        doc.close()

        return info