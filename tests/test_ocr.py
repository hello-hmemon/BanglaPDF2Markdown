from tests.conftest import SAMPLE_PDF

from bp2md.ocr import OCRProcessor

pdf = SAMPLE_PDF

ocr = OCRProcessor()

out = ocr.run(pdf)

print(out)