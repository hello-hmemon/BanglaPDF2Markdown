from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Decision:
    use_ocr: bool
    reason: str


class DecisionEngine:

    def decide(
        self,
        *,
        has_text: bool,
        quality_score: int,
    ) -> Decision:

        if not has_text:
            return Decision(
                use_ocr=True,
                reason="No text layer",
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