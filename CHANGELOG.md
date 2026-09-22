# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-09-22

Production server sync — the repository now matches the live deployment at [drkaman.ir](https://drkaman.ir).

### Added
- **SEO endpoints** (`core/seo_views.py`): `robots.txt` (explicit AI-crawler rules), auto-generated `sitemap.xml`, and `llms.txt`.
- **Production settings** (`dr_kaman_site/settings_prod.py`): `DEBUG=False`, trusted hosts, reverse-proxy HTTPS headers, secure session/CSRF cookies, 100 MB upload limits.
- **Sitemap template** (`templates/core/sitemap.xml`).
- **Responsive stylesheet** (`static/css/responsive.css`).
- Migration `0003` for **audios** — `mp4` added to the allowed podcast formats.
- Migration `0003` for **books** — book file is now optional (`blank=True`, `null=True`), cover extended to `jpg`/`jpeg`/`png`/`webp`.

### Changed
- Homepage and list templates updated to the production versions.
- README rewritten with verified feature list, live-site link, real allowed-format table and screenshots.
- `.gitignore` merged into a superset (adds `.venv/`, `.env`, `*.log`, `.DS_Store`).

### Removed
- Tracked `__pycache__/` and `*.pyc` files from the repository.

## [1.0.0] - 2026-07-03

### Added
- Initial release of Dr. Kaman Psychology Portal.
- **Dynamic Homepage:** Auto-updating slider with latest content.
- **Multimedia Archive:**
  - Audio Works (lectures, podcasts, meditations).
  - Video Works (workshops, interviews, educational series).
  - Book Repository (published books, summaries, recommended reading).
  - Text Archive (articles, essays, research papers).
- **Smart Categorization:** content organization by topic with filtering.
- **Advanced Search:** search across texts, audio and video.
- **Dynamic Content Management:** Admin panel to update "About" and "Contact" pages without code changes.
- **Responsive Design:** Mobile-friendly interface with Persian RTL support.
- **Modern UI:** Clean, professional design focused on readability and accessibility.

### Technical Details
- **Built with:** Django 4.2+, Python 3.10+
- **Database:** SQLite (ready for PostgreSQL upgrade)
- **Features:** Custom sliders, dynamic pages, media management
- **License:** MIT
