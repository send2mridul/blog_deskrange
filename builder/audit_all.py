"""Comprehensive audit script for all 500 DeskRange static blog articles.
Validates each file against Humanizer and Medium-Writer rules.
"""

from pathlib import Path
from builder.humanizer_validator import validate_article_html

ARTICLES_DIR = Path("C:/Users/2025/blog_deskrange/articles")

files = list(ARTICLES_DIR.glob("*.html"))
print(f"Auditing {len(files)} article files...")

passed = 0
failed = 0
total_words = 0

for file_path in files:
    content = file_path.read_text(encoding="utf-8")
    words = len(content.split())
    total_words += words
    
    valid, errors = validate_article_html(content, filename=file_path.name)
    if valid:
        passed += 1
    else:
        failed += 1
        print(f"FAILED: {file_path.name}: {errors}")

print("--------------------------------------------------")
print(f"Total articles audited: {len(files)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Estimated total word count across corpus: {total_words:,} words")
print(f"Average words per article: {total_words // max(1, len(files)):,} words")
print("--------------------------------------------------")
