from __future__ import annotations

import re


class BanglaRepair:

    def repair(self, text: str) -> str:

        text = self.fix_unicode_order(text)
        text = self.fix_spaces(text)
        text = self.fix_punctuation(text)

        return text

    def fix_unicode_order(self, text: str) -> str:

        replacements = {
            "াি": "িা",
            "েি": "িে",
            "োি": "িো",
            "ৌি": "িৌ",
            "্্": "্",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text

    def fix_spaces(self, text: str) -> str:

        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r" *\n *", "\n", text)

        return text.strip()

    def fix_punctuation(self, text: str) -> str:

        text = text.replace("।।", "।")

        return text