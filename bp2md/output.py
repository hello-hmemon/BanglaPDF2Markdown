from __future__ import annotations

import json
from pathlib import Path

from bp2md.config import (
    OUTPUT_DIR,
    SAVE_JSON,
    SAVE_MARKDOWN,
    SAVE_TEXT,
)


class OutputManager:

    def save_text(
        self,
        extractor: str,
        pdf: Path,
        text: str,
    ) -> Path:

        folder = OUTPUT_DIR / extractor.lower().replace(" ", "_")

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = folder / f"{pdf.stem}.txt"

        if SAVE_TEXT:

            path.write_text(
                text,
                encoding="utf-8",
            )

        return path

    def save_markdown(
        self,
        extractor: str,
        pdf: Path,
        text: str,
    ) -> Path:

        folder = OUTPUT_DIR / extractor.lower().replace(" ", "_")

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = folder / f"{pdf.stem}.md"

        if SAVE_MARKDOWN:

            path.write_text(
                text,
                encoding="utf-8",
            )

        return path

    def save_json(
        self,
        extractor: str,
        pdf: Path,
        data: dict,
    ) -> Path:

        folder = OUTPUT_DIR / extractor.lower().replace(" ", "_")

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = folder / f"{pdf.stem}.json"

        if SAVE_JSON:

            path.write_text(
                json.dumps(
                    data,
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )

        return path
