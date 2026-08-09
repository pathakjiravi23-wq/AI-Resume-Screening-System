import re


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line for line in text.splitlines() if line.strip())
    text = re.sub(
        r"Page\s+\d+\s+(?:of\s+\d+)?", "", text, flags=re.IGNORECASE
    )  # (?:  ) will not save groups or capture groups
    text = re.sub(r"[ \t]+", " ", text)  # [" " or \t]
    text = text.replace("●", "•").replace("▪", "•").replace("‣", "•")

    return text
