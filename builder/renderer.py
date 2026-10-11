"""Renderer for DeskRange Journal static HTML articles.
Converts structured article data into a full, self-contained HTML page
and verifies compliance with Humanizer and Medium-Writer rules.
"""

import html
import re
from pathlib import Path
from typing import Dict, Any
from builder.humanizer_validator import validate_article_html

ARTICLES_DIR = Path("C:/Users/2025/blog_deskrange/articles")
ARTICLES_DIR.mkdir(parents=True, exist_ok=True)


def render_and_save_article(data: Dict[str, Any]) -> str:
    """Renders an article dictionary into an HTML file and saves it."""
    slug = data["slug"]
    title = data["title"]
    subtitle = data["subtitle"]
    category = data["category"]
    seo_title = data["seo_title"]
    seo_description = data["seo_description"]
    tags = data["tags"]
    tags_str = ", ".join(tags)

    # Clean prose to ensure zero forbidden dashes
    def clean_text(text: str) -> str:
        text = text.replace("—", ", ")
        text = text.replace("–", ", ")
        text = text.replace(" -- ", ", ")
        # Ensure straight quotes
        text = text.replace("“", '"').replace("”", '"')
        text = text.replace("‘", "'").replace("’", "'")
        return text

    scene = clean_text(data["scene"])
    sec1_title = clean_text(data["sec1_title"])
    sec1_text = clean_text(data["sec1_text"])
    sec2_title = clean_text(data["sec2_title"])
    sec2_text = clean_text(data["sec2_text"])
    sec3_title = clean_text(data["sec3_title"])
    sec3_text = clean_text(data["sec3_text"])
    sec4_title = clean_text(data["sec4_title"])
    sec4_text = clean_text(data["sec4_text"])
    sec5_title = clean_text(data["sec5_title"])
    sec5_text = clean_text(data["sec5_text"])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} | DeskRange Journal</title>
  <meta name="description" content="{html.escape(seo_description)}">
  <meta name="keywords" content="{html.escape(tags_str)}">
  <link rel="canonical" href="https://blog.deskrange.aibucket.org/articles/{slug}.html">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(seo_description)}">
  <meta property="og:url" content="https://blog.deskrange.aibucket.org/articles/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="DeskRange Journal">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(title)}">
  <meta name="twitter:description" content="{html.escape(seo_description)}">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{html.escape(title)}",
    "description": "{html.escape(seo_description)}",
    "keywords": "{html.escape(tags_str)}",
    "url": "https://blog.deskrange.aibucket.org/articles/{slug}.html",
    "author": {{
      "@type": "Organization",
      "name": "DeskRange Journal Editorial Team",
      "url": "https://deskrange.aibucket.org/"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "DeskRange AI",
      "url": "https://deskrange.aibucket.org/",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://deskrange.aibucket.org/icon-192.png"
      }}
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://blog.deskrange.aibucket.org/articles/{slug}.html"
    }}
  }}
  </script>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="../index.html" class="logo">DeskRange <span>Journal</span></a>
      <nav class="nav-links">
        <a href="../index.html">All Articles</a>
        <a href="../sitemap.html">Index &amp; Topics</a>
        <a href="https://deskrange.aibucket.org/" class="btn-primary" target="_blank" rel="noopener">Try DeskRange AI</a>
      </nav>
    </div>
  </header>

  <main class="article-wrapper">
    <section id="metadata">
      <p><strong>Title:</strong> {title}</p>
      <p><strong>Subtitle:</strong> {subtitle}</p>
      <p><strong>SEO Title:</strong> {seo_title}</p>
      <p><strong>SEO Description:</strong> {seo_description}</p>
      <p><strong>Tags:</strong> {tags_str}</p>
    </section>

    <article>
      <h1>{title}</h1>
      <p class="article-deck"><em>{subtitle}</em></p>
      <div class="article-meta-bar">
        <span>Category: {category}</span> &bull; <span>DeskRange Health &amp; Ergonomics Team</span>
      </div>

      {scene}

      <h2>{sec1_title}</h2>
      {sec1_text}

      <h2>{sec2_title}</h2>
      {sec2_text}

      <h2>{sec3_title}</h2>
      {sec3_text}

      <h2>{sec4_title}</h2>
      {sec4_text}

      <h2>{sec5_title}</h2>
      {sec5_text}

      <section class="footnote-section">
        <h2>Author Note and Field Reference</h2>
        <p>This article is part of the DeskRange Ergonomics Research series, examining how computer workers, software engineers, and digital creatives can maintain spinal health and focus over decades of computer work. For private on-device posture feedback that learns your natural posture range without cloud video recording, visit <a href="https://deskrange.aibucket.org/">DeskRange AI</a>.</p>
      </section>
    </article>

    <nav class="related-nav">
      <div class="related-box">
        <h3>Explore More Ergonomics Guides</h3>
        <p>Browse through 500 research-backed articles on desk health, monitor geometry, chair mechanics, and private posture coaching in the <a href="../sitemap.html">DeskRange Article Index</a> or return to the <a href="../index.html">Journal Homepage</a>.</p>
      </div>
    </nav>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <p>&copy; 2026 DeskRange AI. Private, on-device posture coaching for Windows.</p>
      <p><a href="https://deskrange.aibucket.org/">DeskRange AI Home</a> &bull; <a href="../sitemap.html">Sitemap &amp; Topics</a> &bull; <a href="../index.html">All Articles</a></p>
    </div>
  </footer>

  <script src="../script.js"></script>
</body>
</html>
"""

    valid, errors = validate_article_html(html_content, filename=f"{slug}.html")
    if not valid:
        raise ValueError(f"Validation failed for {slug}.html: {errors}")

    file_path = ARTICLES_DIR / f"{slug}.html"
    file_path.write_text(html_content, encoding="utf-8")
    return str(file_path)
