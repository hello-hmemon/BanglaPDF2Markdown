from __future__ import annotations

from pathlib import Path


# ==========================================================
# Project
# ==========================================================

APP_NAME = "BanglaPDF2Markdown"

VERSION = "1.0.0"


# ==========================================================
# Directories
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DIR = PROJECT_ROOT / "input"

OUTPUT_DIR = PROJECT_ROOT / "output"

BENCHMARK_DIR = OUTPUT_DIR / "benchmark"

FINAL_DIR = OUTPUT_DIR / "final"


# ==========================================================
# Create Directories
# ==========================================================

INPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

BENCHMARK_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

FINAL_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# ==========================================================
# OCR
# ==========================================================

OCR_ENABLED = True

OCR_LANGUAGE = "ben+eng"

OCR_THRESHOLD = 60

OCR_MODE = "skip-text"


# ==========================================================
# Extractors
# ==========================================================

DEFAULT_EXTRACTOR = "PDFPlumber"

EXTRACTOR_TIMEOUT = 60


# ==========================================================
# Output
# ==========================================================

SAVE_TEXT = True

SAVE_MARKDOWN = True

SAVE_JSON = False


# ==========================================================
# Quality
# ==========================================================

QUALITY_PASS_SCORE = 80

QUALITY_WARNING_SCORE = 60


# ==========================================================
# Logging
# ==========================================================

VERBOSE = True
