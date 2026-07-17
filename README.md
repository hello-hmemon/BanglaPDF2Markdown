# BanglaPDF2Markdown

> Smart Bangla PDF to Markdown extraction pipeline with OCR,
> benchmarking and Bangla Unicode repair.

!\[Python](https://img.shields.io/badge/Python-3.11%2B-blue)
!\[License](https://img.shields.io/badge/License-MIT-green)
!\[Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

Repository: https://github.com/hello-hmemon/BanglaPDF2Markdown

\---

## Features

* Automatic PDF analysis
* Smart OCR decision (OCR only when needed)
* Four extraction engines:

  * PyMuPDF
  * PDFPlumber
  * Poppler (pdftotext)
  * MarkItDown
* Bangla Unicode repair engine
* Automatic quality scoring
* Benchmark comparison
* CSV \& SQLite logging
* TXT and Markdown export

\---

## Installation

``` bash
git clone https://github.com/hello-hmemon/BanglaPDF2Markdown.git
cd BanglaPDF2Markdown

python -m venv .venv

# Windows
.venv\\Scripts\\activate

pip install -r requirements.txt
```

### External tools

Install if OCR support is required:

* Tesseract OCR
* OCRmyPDF
* Poppler

\---

## Usage

``` bash
python app.py sample.pdf
```

Absolute path:

``` bash
python app.py "D:\\PDF Test Files\\book.pdf"
```

\---

## Pipeline

``` text
PDF
 │
 ▼
Analyze PDF
 │
 ▼
OCR Decision
 │
 ▼
Run Extractors
 │
 ▼
Unicode Repair
 │
 ▼
Quality Score
 │
 ▼
Benchmark
 │
 ▼
Final TXT / Markdown
```

\---

## Extractors

Extractor    Notes

\---

PyMuPDF      Fast
PDFPlumber   High text quality
Poppler      Better table/layout preservation
MarkItDown   Markdown friendly

Poppler is preferred for the final output when available because it
preserves tables and layout better, while benchmark ranking still uses
quality scores.

\---

## Output

``` text
output/
├── benchmark/
│   ├── pymupdf/
│   ├── pdfplumber/
│   ├── poppler/
│   └── markitdown/
├── final/
│   ├── sample.txt
│   └── sample.md
├── benchmark.csv
└── benchmark.db
```

\---

## Project Structure

``` text
BanglaPDF2Markdown/
├── bp2md/
├── extractors/
├── tests/
├── output/
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── README.md
```

\---

## Configuration

Most settings are available in:

``` text
bp2md/config.py
```

Examples:

* OCR language
* OCR threshold
* Output options
* Verbose mode

\---

## Roadmap

* \[x] Multi-extractor benchmark
* \[x] OCR pipeline
* \[x] Unicode repair
* \[x] CSV logging
* \[x] SQLite logging
* \[ ] Batch processing
* \[ ] HTML export
* \[ ] DOCX export
* \[ ] GUI
* \[ ] Better table reconstruction

\---

## Contributing

Issues and pull requests are welcome.

\---

## License

Released under the MIT License.

\---

## Author

**H M Nuruddin Mahamud Emon**

GitHub: https://github.com/hello-hmemon

