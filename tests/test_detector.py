from tests.conftest import SAMPLE_PDF

from bp2md.pdf_detector import PDFDetector

detector = PDFDetector()

info = detector.analyze(SAMPLE_PDF)

print("PDF Analysis")
print("-" * 30)

print(f"Pages        : {info.pages}")
print(f"Text Layer   : {info.has_text}")
print(f"Tagged       : {info.tagged}")
print(f"Encrypted    : {info.encrypted}")

print(f"Characters   : {info.characters:,}")
print(f"Bangla       : {info.bangla_chars:,}")
print(f"English      : {info.english_chars:,}")
print(f"Images       : {info.images}")
print(f"Corruption   : {info.corruption:.2f}%")