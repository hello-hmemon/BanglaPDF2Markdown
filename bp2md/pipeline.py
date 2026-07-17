from __future__ import annotations

from pathlib import Path

from bp2md.decision import DecisionEngine
from bp2md.pdf_detector import PDFDetector
from bp2md.runner import BenchmarkRunner
from bp2md.ocr import OCRProcessor


class ExtractionPipeline:

    def __init__(self):

        self.detector = PDFDetector()
        self.decision = DecisionEngine()
        self.ocr = OCRProcessor()
        self.runner = BenchmarkRunner()

    def run(self, pdf: Path):

        print("\nAnalyzing PDF...")

        info = self.detector.analyze(pdf)

        print(f"Pages      : {info.pages}")
        print(f"Text Layer : {info.has_text}")
        print(f"Encrypted  : {info.encrypted}")

        decision = self.decision.decide(
            info=info,
            quality_score=100,
        )

        print(f"\nDecision : {decision.reason}")

        process_pdf = pdf

        if decision.use_ocr:

            print("OCR Applied")

            process_pdf = self.ocr.run(pdf)

        else:

            print("OCR Not Needed")

        print("\nStarting Extraction Benchmark...")

        results = self.runner.run(process_pdf)

        return results
