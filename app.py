def process_pdf(pdf: Path):

    if not pdf.exists():
        print(f"[ERROR] File not found: {pdf}")
        return

    print(f"\n{'=' * 60}")
    print(pdf.name)
    print("=" * 60)

    hybrid = HybridOCR()

    pdf_to_process, used_ocr = hybrid.process(pdf)

    if used_ocr:
        print("OCR Applied")
    else:
        print("OCR Not Needed")

    runner = BenchmarkRunner()
    runner.run(pdf_to_process)