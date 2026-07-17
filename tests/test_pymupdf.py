from tests.conftest import SAMPLE_PDF

from extractors.pymupdf_ext import PyMuPDFExtractor

pdf = SAMPLE_PDF

extractor = PyMuPDFExtractor()

result = extractor.extract(pdf)

print(result.extractor)
print(result.success)
print(result.error)
print(result.text[:1000])
