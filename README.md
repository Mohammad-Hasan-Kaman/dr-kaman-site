# 🧠 Dr. Kaman Psychology Portal

> A professional multi-media archive for Dr. Mohammad Reza Kaman, featuring podcasts, videos, books, and articles with advanced search capabilities.

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg?logo=django&logoColor=white)](https://django.com)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/Mohammad-Hasan-Kaman/dr-kaman-site?color=blue)](https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site/releases)
[![Live](https://img.shields.io/badge/Live-drkaman.ir-2ecc71.svg)](https://drkaman.ir)

---

## 🚀 Purpose & Audience

This project is designed for **"Seamless access to psychological content"**:

| Audience | How to Use |
|----------|------------|
| **General Public** | Visit the live website: **[drkaman.ir](https://drkaman.ir)** |
| **Developers** | Clone the source code, run locally for study, development, or customization. |

---

## ✨ Key Features

- 🎨 **Modern UI with Persian Font Support:** Uses `BMitra` font for correct and beautiful Persian text rendering.
- 🎧 **Comprehensive Multi-Media Archive:**
  - **Podcasts (`AudioWork`):** audio files with topic categorization.
  - **Videos (`VideoWork`):** educational videos and lectures.
  - **Books (`Book`):** PDF/EPUB files with cover images (file itself is optional).
  - **Articles (`TextWork`):** textual, Word and PDF research content.
- 🔍 **Cross-Media Search:** one query against titles and descriptions of texts, podcasts and videos (`search` app).
- 📂 **Categorization:** organize content by topic (Psychology, Therapy, Self-Help, Mindfulness, etc.).
- 🎬 **Dynamic Slider:** highlight important or new items on the homepage, with an optional clickable link per slide.
- 📄 **Dynamic Pages (editable from the admin panel):**
  - **About Us:** Dr. Kaman's bio.
  - **Contact Us:** contact form plus phone / email / address.
- 🌐 **SEO Endpoints** (`core/seo_views.py`):
  - `robots.txt` — explicit allow rules for search engines and AI crawlers (GPTBot, ClaudeBot, PerplexityBot, …).
  - `sitemap.xml` — auto-generated from the latest 100 items of each content type.
  - `llms.txt` — machine-readable site summary for LLMs.
- 🛡 **Security & Validation:**
  - File-format validation per content type (see table below).
  - Automatic media file management in designated folders.
- 📱 **Responsive Design:** displays correctly on mobile, tablet, and desktop (`static/css/responsive.css`).
- ⚙️ **Separate Production Settings:** `dr_kaman_site/settings_prod.py` inherits from `settings.py` and adds `DEBUG=False`, HTTPS-aware proxy headers, secure cookies and 100 MB upload limits.

### Allowed upload formats (verified in `models.py`)

| Content type | File field | Allowed extensions |
|--------------|-----------|--------------------|
| Podcast | `AudioWork.audio_file` | `mp3`, `wav`, `ogg`, `m4a`, `mp4` |
| Video | `VideoWork.video_file` | `mp4`, `mkv`, `mov`, `avi`, `webm` |
| Book | `Book.book_file` | `pdf`, `epub` (optional) |
| Book cover | `Book.cover_image` | `jpg`, `jpeg`, `png`, `webp` |
| Article | `TextWork.file` | `pdf`, `doc`, `docx`, `txt`, `epub` |
| Slider / video thumb | `Slider.image`, `VideoWork.slider_image` | image formats via Pillow |

---

## 📥 Installation & Setup

### 1. For General Users (Live Website)

**🌐 [https://drkaman.ir](https://drkaman.ir)**

### 2. For Developers (Local Setup)

```bash
# Clone the repository
git clone https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site.git
cd dr-kaman-site

# Create a virtual environment (recommended)
python -m venv venv
# Activate it:
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (create database tables)
python manage.py migrate

# Create an admin user for the panel
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Run the development server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000` in your browser.

### 3. Production (how it runs on the server)

The site is served with `gunicorn` behind `nginx`, using the dedicated settings module:

```bash
python manage.py migrate --settings=dr_kaman_site.settings_prod
python manage.py collectstatic --noinput --settings=dr_kaman_site.settings_prod
gunicorn dr_kaman_site.wsgi --settings=dr_kaman_site.settings_prod
```

`settings_prod.py` reads the host name from the environment and keeps `settings.py` untouched.

---

## 🛠 Tech Stack

| Technology | Role |
|------------|------|
| **Django 4.2+** | Main Web Framework (MVC Pattern) |
| **Python 3.10+** | Programming Language |
| **SQLite** | Default Database (Configurable to PostgreSQL for Production) |
| **Pillow** | Image Processing (for book covers and sliders) |
| **python-dotenv** | Optional environment-variable loading |
| **BMitra Font** | Professional Persian typography |
| **HTML5/CSS3** | Frontend Templates (RTL, `fa-ir`) |

---

## 📸 Screenshots

| Homepage | Content Gallery | Search |
|----------|-----------------|--------|
| ![Homepage](assets/screenshot_home.svg) | ![Gallery](assets/screenshot_gallery.svg) | ![Search](assets/screenshot_search.svg) |

> Placeholder illustrations of the layout. Real screenshots can be dropped into `assets/` to replace them.

---

## 📝 Project Structure

```
dr-kaman-site/
├── assets/                  # Graphics and screenshots
├── audios/                  # Podcast app
├── books/                   # Book app
├── categories/              # Content categorization
├── core/                    # Main app (slider, about, contact)
│   ├── seo_views.py         # robots.txt / sitemap.xml / llms.txt
│   └── models.py            # Slider, AboutPage, ContactPage
├── dr_kaman_site/           # Project configuration
│   ├── settings.py          # Development settings
│   └── settings_prod.py     # Production settings (HTTPS, secure cookies)
├── search/                  # Cross-media search engine
├── static/                  # Static files (CSS, JS, Fonts)
├── templates/               # HTML templates (incl. core/sitemap.xml)
├── texts/                   # Articles app
├── videos/                  # Videos app
├── test_upload.py           # Upload helper scripts used on the server
├── test_large_upload.py
├── CHANGELOG.md             # Changelog
├── CONTRIBUTING.md          # Contribution guide
├── LICENSE                  # MIT License
├── README.md                # This file
├── requirements.txt         # Python dependencies
└── manage.py                # Django management script
```

---

## 📂 Database & Media

- **Database:** Default is `db.sqlite3`. For production, we recommend switching to **PostgreSQL**.
- **Media Files:** Uploaded files (videos, audio, books) are stored in the `media/` directory and managed via `MEDIA_URL` and `MEDIA_ROOT` in settings.
- Both `db.sqlite3` and `media/` are git-ignored; they exist only on the server.

---

## 🤝 Contributing

If you find a bug or have a suggestion, please open an [Issue](https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site/issues).
Developers are welcome to contribute! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## ⭐ Support

If you find this project useful, please give it a **⭐ star**!
Thank you for your support.

[![Stars](https://img.shields.io/github/stars/Mohammad-Hasan-Kaman/dr-kaman-site?style=for-the-badge&logo=github&color=blue)](https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site/stargazers)

---

*Maintained by Mohammad Hasan Kaman | Last updated: September 2026*

> **Disclaimer:** This project is designed for educational and archival purposes only. All content belongs to Dr. Mohammad Reza Kaman.
