"""Guardrails for the toy assistant. Complete the TODOs."""
import re

# TODO 1: add more suspicious phrases that attackers might use.
SUSPICIOUS_PATTERNS = [
    r"ignore (all )?(previous|prior) instructions",
]

SECRET_PATTERN = r"sk-[a-z0-9-]+"


def check_input(text: str) -> bool:
    """Return True if the input looks safe, False if it should be blocked."""
    return not any(re.search(p, text, re.IGNORECASE) for p in SUSPICIOUS_PATTERNS)


def check_output(text: str) -> bool:
    """Return True if the output is safe to show.

    TODO 2: block any reply that contains something matching SECRET_PATTERN.
    (Output scanning still works when the attacker finds a phrasing your input filter misses.)
    """
    return True
