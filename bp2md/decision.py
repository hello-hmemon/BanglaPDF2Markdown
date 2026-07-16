from __future__ import annotations

from dataclasses import dataclass

from bp2md.pdf_detector import PDFInfo


@dataclass(slots=True)
class Decision:
    use_ocr: bool
    reason: str


class DecisionEngine:

    def decide(
        self,
        info: PDFInfo,
        quality_score: int,
    ) -> Decision:

        if info.encrypted:
            return Decision(
                use_ocr=False,
                reason="Encrypted PDF",
            )

        if not info.has_text:
            return Decision(
                use_ocr=True,
                reason="No text layer",
            )

        if info.corruption > 10:
            return Decision(
                use_ocr=True,
                reason=f"Corruption {info.corruption:.1f}%",
            )

        if quality_score < 60:
            return Decision(
                use_ocr=True,
                reason=f"Low quality ({quality_score})",
            )

        return Decision(
            use_ocr=False,
            reason="Normal extraction",
        )