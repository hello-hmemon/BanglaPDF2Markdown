from __future__ import annotations

import argparse
from pathlib import Path

from bp2md.config import (
    APP_NAME,
    VERSION,
    INPUT_DIR,
)
from bp2md.pipeline import ExtractionPipeline


def process_pdf(pdf: Path):

    if not pdf.exists():

        candidate = INPUT_DIR / pdf.name

        if candidate.exists():
            pdf = candidate

        else:
            print(f"[ERROR] File not found: {pdf}")
            return

    print("\n" + "=" * 60)
    print(pdf.name)
    print("=" * 60)

    pipeline = ExtractionPipeline()

    pipeline.run(pdf)


def process_folder(folder: Path):

    pdfs = sorted(
        folder.glob("*.pdf")
    )

    if not pdfs:

        print("No PDF files found.")
        return

    for pdf in pdfs:

        process_pdf(pdf)


def main():

    parser = argparse.ArgumentParser(
        prog=APP_NAME,
        description=f"{APP_NAME} v{VERSION}",
    )

    parser.add_argument(
        "input",
        help="PDF file or folder",
    )

    args = parser.parse_args()

    path = Path(args.input)

    if path.is_file():

        process_pdf(path)

    elif path.is_dir():

        process_folder(path)

    else:

        process_pdf(path)


if __name__ == "__main__":

    main()
