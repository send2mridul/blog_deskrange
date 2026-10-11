"""Humanizer and Medium-Writer Validator for DeskRange Blog Articles.
Validates HTML article packages against rules in .codex/skills/humanizer and medium-writer.
"""

import re
from typing import List, Tuple

FORBIDDEN_WORDS = [
    r"\bdelve\b", r"\bdelving\b", r"\bdelved\b",
    r"\btapestry\b",
    r"\bpivotal\b",
    r"\bcrucial\b",
    r"\blandscape\b",
    r"\btestament\b",
    r"\bbolster\b", r"\bbolstered\b",
    r"\bmeticulous\b", r"\bmeticulously\b",
    r"\bshowcase\b", r"\bshowcasing\b",
    r"\bvibrant\b",
    r"\brobust\b",
    r"\bfoster\b", r"\bfostering\b",
    r"\binterplay\b",
    r"\bintricate\b", r"\bintricacies\b",
    r"\bunderscore\b", r"\bunderscores\b", r"\bunderscoring\b",
    r"\brevolutionize\b", r"\bgame-changing\b", r"\bgroundbreaking\b",
    r"\bbeacon\b", r"\bunwavering\b", r"\bnestled\b",
]

FORBIDDEN_PHRASES = [
    r"let's dive in", r"dive deep", r"deep dive",
    r"here's what you need to know",
    r"without further ado",
    r"let's be honest",
    r"real talk",
    r"the thing is",
    r"here's the thing",
    r"in plain english",
    r"put simply",
    r"simply put",
    r"what this means is",
    r"to be clear",
    r"don't get me wrong",
    r"you might think",
    r"some might say",
    r"this is not to say",
    r"that is the real win",
    r"read that again",
    r"let that sink in",
    r"i hope this helps",
    r"great question",
    r"you're absolutely right",
    r"as an ai",
]

FORBIDDEN_CHARS = [
    "—",  # em dash
    "–",  # en dash
    " -- ", # double hyphen dash
]


def validate_article_html(html_content: str, filename: str = "") -> Tuple[bool, List[str]]:
    """Validates an article against Humanizer and Medium-Writer rules."""
    errors = []

    # 1. Check forbidden characters (dashes)
    for char in FORBIDDEN_CHARS:
        if char in html_content:
            errors.append(f"Forbidden dash character found: {repr(char)}")

    # 2. Check forbidden words
    content_lower = html_content.lower()
    for word_pattern in FORBIDDEN_WORDS:
        match = re.search(word_pattern, content_lower)
        if match:
            errors.append(f"Forbidden AI word detected: '{match.group(0)}'")

    # 3. Check forbidden phrases
    for phrase_pattern in FORBIDDEN_PHRASES:
        if re.search(phrase_pattern, content_lower):
            errors.append(f"Forbidden AI phrase detected: '{phrase_pattern}'")

    # 4. Check HTML structure requirements
    if '<section id="metadata">' not in html_content:
        errors.append("Missing <section id=\"metadata\"> block")
    if '<strong>Title:</strong>' not in html_content:
        errors.append("Missing Title in metadata block")
    if '<strong>Subtitle:</strong>' not in html_content:
        errors.append("Missing Subtitle in metadata block")
    if '<strong>SEO Title:</strong>' not in html_content:
        errors.append("Missing SEO Title in metadata block")
    if '<strong>SEO Description:</strong>' not in html_content:
        errors.append("Missing SEO Description in metadata block")
    if '<strong>Tags:</strong>' not in html_content:
        errors.append("Missing Tags in metadata block")

    if "<article>" not in html_content or "</article>" not in html_content:
        errors.append("Missing <article> wrapper")

    h1_count = len(re.findall(r"<h1[^>]*>", html_content))
    if h1_count != 1:
        errors.append(f"Expected exactly 1 <h1> tag, found {h1_count}")

    h2_count = len(re.findall(r"<h2[^>]*>", html_content))
    if h2_count < 5:
        errors.append(f"Expected at least 5 <h2> sections, found {h2_count}")

    # Check natural mention of DeskRange AI
    if "deskrange.aibucket.org" not in html_content:
        errors.append("Missing link to deskrange.aibucket.org")

    # Check Footnote
    if "footnote" not in content_lower and "author note" not in content_lower:
        errors.append("Missing author note / footnote section")

    return len(errors) == 0, errors


if __name__ == "__main__":
    sample = """
    <section id="metadata">
    <p><strong>Title:</strong> Testing Posture</p>
    <p><strong>Subtitle:</strong> A test article</p>
    <p><strong>SEO Title:</strong> Testing Posture - Desk Guide</p>
    <p><strong>SEO Description:</strong> A test description for search engines.</p>
    <p><strong>Tags:</strong> Posture, Health, Desk, Ergonomics, Work</p>
    </section>
    <article>
    <h1>Testing Posture</h1>
    <h2>Section One</h2><p>Text.</p>
    <h2>Section Two</h2><p>Text.</p>
    <h2>Section Three</h2><p>Text with https://deskrange.aibucket.org/ link.</p>
    <h2>Section Four</h2><p>Text.</p>
    <h2>Section Five</h2><p>Text.</p>
    <h2>Author Note</h2><p>Footnote here.</p>
    </article>
    """
    valid, errs = validate_article_html(sample)
    print("Sample validation:", "PASS" if valid else f"FAIL: {errs}")
