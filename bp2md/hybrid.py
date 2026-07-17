from __future__ import annotations

from pathlib import Path

from bp2md.decision import DecisionEngine
from bp2md.ocr import OCRProcessor
from bp2md.pdf_detector import PDFDetector


class HybridOCR:

    def __init__(self):

        self.detector = PDFDetector()
        self.decision = DecisionEngine()
        self.ocr = OCRProcessor()

    def process(self, pdf: Path) -> tuple[Path, bool]:

        info = self.detector.analyze(pdf)

        decision = self.decision.decide(info, 100)

        print(f"\nDecision : {decision.reason}")

        if decision.use_ocr:

            print("Running OCR...")

            pdf = self.ocr.run(pdf)

            return pdf, True

        return pdf, False