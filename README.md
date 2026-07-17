\# BanglaPDF2Markdown



A smart PDF extraction and conversion pipeline focused on \*\*Bangla PDF documents\*\*.



BanglaPDF2Markdown automatically detects PDF quality, selects the best extraction method, repairs common Bangla Unicode ordering issues, and exports clean text/Markdown output.



\---



\## Features



\### PDF Analysis

\- Detect text layer availability

\- Detect encrypted PDFs

\- Analyze PDF structure

\- Estimate extraction quality



\### Smart OCR Decision

\- Automatically decides whether OCR is required

\- Supports Bangla + English OCR

\- Avoids unnecessary OCR on digital PDFs



\### Multiple Extraction Engines



Supported extractors:



\- PyMuPDF

\- PDFPlumber

\- Poppler (`pdftotext`)

\- Microsoft MarkItDown



Each extractor is benchmarked automatically.



\---



\## Bangla Text Repair



Bangla PDFs often contain Unicode ordering problems.



Example:


Before: শবদ্যািয়

After: বিদ্যালয়



Built-in repair rules fix common issues:

- `াি → ি`
- `েি → ি`
- `োি → ি`
- `ৌি → ি`
- `।। → ।`

---

## Quality Scoring

Every extraction is evaluated using:

- Bangla character count
- Replacement issues
- Unicode corruption patterns
- Text quality score

Example:

Score Before : 78/100
Score After : 100/100



---

## Output Structure

After processing:
output/

├── benchmark/
│
│ ├── pymupdf/
│ ├── pdfplumber/
│ ├── poppler/
│ └── markitdown/
│
├── final/
│
│ ├── sample.txt
│ └── sample.md
│
├── benchmark.csv
└── benchmark.db


---

## Installation

Clone repository:

```bash
git clone <repository-url>

cd BanglaPDF2Markdown



Install dependencies:

pip install -r requirements.txt



Requirements

Python:

Python 3.11+



External tools:

Poppler

Required for pdftotext.

Windows:

Install Poppler and add:

Library/bin

to PATH.


Tesseract OCR

Required for scanned PDFs.

Install:

Tesseract OCR
Bangla language pack

Language:

ben+eng


Usage

Single PDF:

python app.py sample.pdf


PDF inside input folder:

python app.py input/sample.pdf


Folder processing:

python app.py input/


Example


Analyzing PDF...

Pages      : 3
Text Layer : True

Decision : Normal extraction

Running PDFPlumber...

Score Before : 78/100
Score After  : 100/100

Winner : PDFPlumber

Final TXT : output/final/sample.txt
Final MD  : output/final/sample.md


Database

Benchmark results are stored in:

output/benchmark.db


Open with:

DB Browser for SQLite


Project Structure


BanglaPDF2Markdown/

├── app.py
│
├── bp2md/
│   ├── detector
│   ├── OCR
│   ├── repair engine
│   ├── quality scorer
│   ├── pipeline
│   └── output manager
│
├── extractors/
│   ├── pymupdf
│   ├── pdfplumber
│   ├── poppler
│   └── markitdown
│
├── tests/
│
├── input/
│
└── output/


Version

Current: v1.0.0


License

MIT License


---