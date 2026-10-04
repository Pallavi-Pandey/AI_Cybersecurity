"""Guardrails for the toy assistant: SOLUTION."""
import re

# TODO 1 solution: a wider list of injection phrasings.
SUSPICIOUS_PATTERNS = [
    r"ignore (all )?(previous|prior|above) instructions",
    r"disregard (all )?(previous|prior|above|your) (instructions|rules)",
    r"forget (everything|all|your) (above|previous|instructions|rules)",
    r"you are now",
    r"(reveal|print|show|leak|output|tell me).{0,30}(api key|secret|password|system prompt)",
    r"system prompt",
]

SECRET_PATTERN = r"sk-[a-z0-9-]+"


def check_input(text: str) -> bool:
    """Return True if the input looks safe, False if it should be blocked."""
    return not any(re.search(p, text, re.IGNORECASE) for p in SUSPICIOUS_PATTERNS)


def check_output(text: str) -> bool:
    """TODO 2 solution: block any reply containing something that looks like the secret."""
    return re.search(SECRET_PATTERN, text, re.IGNORECASE) is None
