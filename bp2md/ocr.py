from __future__ import annotations

import subprocess
from pathlib import Path

from bp2md.config import OCR_LANGUAGE


class OCRProcessor:

    def run(self, pdf: Path) -> Path:

        output = pdf.with_stem(pdf.stem + "_ocr")

        cmd = [
            "ocrmypdf",
            "--skip-text",
            "-l",
            OCR_LANGUAGE,
            str(pdf),
            str(output),
        ]

        subprocess.run(
            cmd,
            check=True,
        )

        return output