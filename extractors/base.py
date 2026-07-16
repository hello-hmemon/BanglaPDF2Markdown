from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class ExtractionResult:
    extractor: str
    text: str
    success: bool
    error: str | None = None

    # Extra information about the extraction
    metadata: dict[str, Any] = field(default_factory=dict)


class BaseExtractor(ABC):

    name: str = "BaseExtractor"

    @abstractmethod
    def extract(self, pdf_path: Path) -> ExtractionResult:
        pass

    def __call__(self, pdf_path: Path) -> ExtractionResult:
        return self.extract(pdf_path)

    def save(self, pdf_path: Path, result: ExtractionResult) -> Path:
        """
        Save extracted text to:

        output/<extractor_name>/<pdf_name>.txt
        """

        from bp2md.config import OUTPUT_DIR

        output_dir = OUTPUT_DIR / self.name.lower().replace(" ", "_")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / f"{pdf_path.stem}.txt"

        output_file.write_text(
            result.text,
            encoding="utf-8",
        )

        return output_file
