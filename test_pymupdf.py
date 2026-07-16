from pathlib import Path

from extractors.pymupdf_ext import PyMuPDFExtractor

pdf = Path("sample.pdf")

extractor = PyMuPDFExtractor()

result = extractor.extract(pdf)

print(result.extractor)
print(result.success)
print(result.error)
print(result.text[:1000])
