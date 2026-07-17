from pathlib import Path

from bp2md.ocr import OCRProcessor

pdf = Path("sample.pdf")

ocr = OCRProcessor()

out = ocr.run(pdf)

print(out)