from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from bp2md.config import EXTRACTOR_TIMEOUT
from bp2md.utils import (
    count_characters,
    count_words,
    normalize_text,
)
from extractors.base import BaseExtractor, ExtractionResult


class PopplerExtractor(BaseExtractor):
    """
    Extract text using Poppler (pdftotext).
    """

    name = "Poppler"

    POPPLER_PATH = None

    def _find_pdftotext(self) -> str:

        if self.POPPLER_PATH:
            return self.POPPLER_PATH

        exe = shutil.which("pdftotext")

        print(f"Using pdftotext: {exe}")

        if exe:
            return exe

        raise FileNotFoundError(
            "pdftotext.exe not found. Install Poppler or add it to PATH."
        )

    def extract(self, pdf_path: Path) -> ExtractionResult:

        try:

            pdftotext = self._find_pdftotext()

            print(f"PDF path: {pdf_path.resolve()}")

            result = subprocess.run(
                [
                    pdftotext,
                    "-layout",
                    "-enc",
                    "UTF-8",
                    str(pdf_path.resolve()),
                    "-",
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=EXTRACTOR_TIMEOUT,
                check=True,
            )

            text = normalize_text(result.stdout)

            return ExtractionResult(
                extractor=self.name,
                text=text,
                success=True,
                metadata={
                    "characters": count_characters(text),
                    "words": count_words(text),
                },
            )

        except FileNotFoundError as e:

            return ExtractionResult(
                extractor=self.name,
                text="",
                success=False,
                error=str(e),
            )

        except subprocess.TimeoutExpired:

            return ExtractionResult(
                extractor=self.name,
                text="",
                success=False,
                error="Poppler timed out.",
            )

        except subprocess.CalledProcessError as e:

            return ExtractionResult(
                extractor=self.name,
                text="",
                success=False,
                error=e.stderr.strip() if e.stderr else str(e),
            )

        except Exception as e:

            return ExtractionResult(
                extractor=self.name,
                text="",
                success=False,
                error=str(e),
            )
