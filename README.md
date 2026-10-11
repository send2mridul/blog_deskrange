# DeskRange Blog & Ergonomics Journal

A comprehensive static publishing platform featuring **500 distinct, in-depth research articles** covering computer ergonomics, spinal biomechanics, chair science, developer posture, and private on-device AI coaching.

Live companion for [DeskRange AI](https://deskrange.aibucket.org/) — private posture coaching for real workdays on Windows.

---

## Corpus Overview

- **Total Static Pages:** 500 dedicated HTML article pages + master index + sitemap
- **Total Word Count:** 480,000+ words across the entire repository
- **Average Article Length:** ~964 words per article (meeting Medium-Writer specifications)
- **Formatting Standards:** Authored in accordance with Medium-Writer and Wikipedia-based Humanizer guidelines (zero AI tell clichés, zero em dashes, authentic voice, rich anatomical metrics).
- **Search & Navigation:** Zero-dependency client-side instant search, tag filtering, and full category browsing.

---

## The 12 Thematic Categories

1. **Biomechanics & Musculoskeletal Anatomy** (45 Articles)
2. **Workstation Setup, Monitor Ergonomics & Hardware** (45 Articles)
3. **Chair Science, Active Seating & Sitting vs Standing** (45 Articles)
4. **Tech Neck, Cervical Spine & Cranial Health** (45 Articles)
5. **Back, Hip & Pelvic Health** (45 Articles)
6. **Software Engineers, Developers & Terminal Workers** (45 Articles)
7. **Gamers, Streamers & Competitive Esports** (40 Articles)
8. **Remote Work, Home Offices & Unconventional Workspaces** (40 Articles)
9. **Specific Professions, Creative Demands & Field Work** (40 Articles)
10. **Movement, Stretches, Microbreaks & Physical Therapy** (40 Articles)
11. **Posture Tech, AI, Computer Vision & Privacy** (40 Articles)
12. **Habits, Psychology, Focus & Longevity** (30 Articles)

---

## Directory Structure

```text
blog_deskrange/
├── index.html            # Main journal portal with instant search and category pills
├── sitemap.html          # Full categorized directory of all 500 articles
├── sitemap.xml           # SEO XML sitemap for web crawlers
├── search-index.json     # Fast client-side search index
├── style.css             # Responsive modern typography stylesheet
├── script.js             # Client-side search and category filtering
├── articles/             # 500 standalone static HTML article pages
│   ├── deep-neck-flexor-fatigue-coding.html
│   ├── upper-crossed-syndrome-desk-workers.html
│   └── ... (500 files)
└── builder/              # Generation and validation toolchain
    ├── humanizer_validator.py
    └── audit_all.py
```

---

## Local Preview

To preview the blog locally:
```bash
# Using Python
python -m http.server 8000

# Open http://localhost:8000 in your browser
```
