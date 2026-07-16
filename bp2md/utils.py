from __future__ import annotations

import re


def normalize_text(text: str) -> str:
    """
    Normalize extracted text from different PDF extractors.
    """

    # Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove trailing whitespace
    lines = [line.rstrip() for line in text.splitlines()]

    # Remove consecutive blank lines
    cleaned: list[str] = []
    previous_blank = False

    for line in lines:

        blank = line.strip() == ""

        if blank:
            if previous_blank:
                continue
            previous_blank = True
        else:
            previous_blank = False

        cleaned.append(line)

    return "\n".join(cleaned).strip()


def count_characters(text: str) -> int:
    """
    Return character count.
    """
    return len(text)


def count_words(text: str) -> int:
    """
    Return word count.
    """
    return len(text.split())


def count_bangla_characters(text: str) -> int:
    """
    Count Bangla Unicode characters.
    """
    return len(re.findall(r"[\u0980-\u09FF]", text))


def count_english_characters(text: str) -> int:
    """
    Count English alphabet characters.
    """
    return len(re.findall(r"[A-Za-z]", text))


def is_mostly_bangla(text: str, threshold: float = 0.5) -> bool:
    """
    Return True if Bangla characters dominate English characters.
    """

    bn = count_bangla_characters(text)
    en = count_english_characters(text)

    total = bn + en

    if total == 0:
        return False

    return (bn / total) >= threshold
