from __future__ import annotations

import re
from pathlib import Path

from bp2md.config import OUTPUT_DIR


class OutputManager:

    def __init__(self):

        self.output_dir = OUTPUT_DIR

        self.benchmark_dir = (
            self.output_dir / "benchmark"
        )

        self.final_dir = (
            self.output_dir / "final"
        )

        self.benchmark_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.final_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _clean_name(self, name: str) -> str:

        name = name.lower()

        name = re.sub(
            r"[^a-z0-9]+",
            "_",
            name,
        )

        return name.strip("_")

    def save_text(
        self,
        extractor: str,
        pdf: Path,
        text: str,
    ) -> Path:

        folder = (
            self.benchmark_dir
            / self._clean_name(extractor)
        )

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        output = folder / f"{pdf.stem}.txt"

        output.write_text(
            text,
            encoding="utf-8",
        )

        return output

    def save_final(
        self,
        pdf: Path,
        text: str,
    ) -> tuple[Path, Path]:

        txt_file = (
            self.final_dir
            / f"{pdf.stem}.txt"
        )

        md_file = (
            self.final_dir
            / f"{pdf.stem}.md"
        )

        txt_file.write_text(
            text,
            encoding="utf-8",
        )

        markdown = (
            f"# {pdf.stem}\n\n"
            f"{text}"
        )

        md_file.write_text(
            markdown,
            encoding="utf-8",
        )

        return txt_file, md_file
