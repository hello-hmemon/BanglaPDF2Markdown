from __future__ import annotations

from pathlib import Path

# ==========================================================
# Project
# ==========================================================

APP_NAME = "BanglaPDF2Markdown"

VERSION = "0.1.0"


# ==========================================================
# Directories
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_DIR = PROJECT_ROOT / "input"

OUTPUT_DIR = PROJECT_ROOT / "output"


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

SAVE_MARKDOWN = False

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
