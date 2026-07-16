from pathlib import Path

from bp2md.detector import PDFDetector

pdf = Path("sample.pdf")


detector = PDFDetector()

result = detector.analyze(pdf)


print("PDF Analysis")
print("----------------")

print("Pages:", result.pages)
print("Text Layer:", result.has_text)
print("Tagged:", result.tagged)

print("Characters:", result.characters)
print("Bangla chars:", result.bangla_characters)

print("Replacement:", result.replacement_count)

print("Corruption:", f"{result.corruption_ratio:.2%}")


if result.ocr_recommended:
    print("\nDecision: OCR Recommended")
else:
    print("\nDecision: Normal Extraction")
