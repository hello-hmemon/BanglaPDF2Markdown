from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"

SAMPLE_PDF = INPUT_DIR / "sample.pdf"
SAMPLE_TXT = OUTPUT_DIR / "pdfplumber" / "sample.txt"