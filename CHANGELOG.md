# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by **Keep a Changelog**, and this project follows
**Semantic Versioning** where applicable.

## \[1.0.0\] - 2026-07-17

### 🎉 Initial Stable Release

### ✨ Added

-   Smart PDF analysis before extraction
-   Automatic OCR decision engine
-   OCR support using OCRmyPDF
-   Multi-extractor benchmarking system
-   Bangla Unicode quality scoring
-   Automatic Bangla Unicode repair engine
-   Automatic best-result selection
-   TXT output generation
-   Markdown output generation
-   CSV benchmark logging
-   SQLite benchmark database
-   Configurable project settings
-   Comprehensive unit tests

### 📄 Supported Extractors

-   PyMuPDF
-   PDFPlumber
-   Poppler (pdftotext)
-   MarkItDown

### 📊 Benchmark Features

-   Extraction time measurement
-   Bangla quality score
-   Character counting
-   Word counting
-   Page counting
-   Automatic ranking
-   Best extractor selection

### 🔤 Bangla Repair

Automatically repairs common Unicode extraction issues, including:

-   Incorrect vowel combinations
-   Duplicate punctuation
-   Duplicate virama
-   Common Bangla PDF extraction artifacts

### 📦 Output

Generated files include:

-   Final TXT
-   Final Markdown
-   Benchmark CSV
-   Benchmark SQLite database

### ⚙️ Configuration

Added configurable options for:

-   OCR language
-   OCR mode
-   OCR threshold
-   Output formats
-   Quality thresholds
-   Verbose logging

## Future Releases

Planned improvements include:

-   Better table reconstruction
-   Batch PDF processing
-   DOCX export
-   HTML export
-   GUI application
-   Web interface
-   Additional extractors
-   Improved Unicode repair rules
-   Enhanced Markdown formatting
