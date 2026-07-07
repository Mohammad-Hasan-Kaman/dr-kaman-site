# 🧠 Dr. Kaman Psychology Portal

> A professional multi-media archive for Dr. Mohammad Reza Kaman, featuring podcasts, videos, books, and articles with advanced search capabilities.

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg?logo=django&logoColor=white)](https://django.com)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/Mohammad-Hasan-Kaman/dr-kaman-site?color=blue)](https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site/releases)

---

## 🚀 Purpose & Audience

This project is designed for **"Seamless access to psychological content"**:

| Audience | How to Use |
|----------|------------|
| **General Public** | Visit the deployed website (Link coming soon) to access content easily. |
| **Developers** | Clone the source code, run locally for study, development, or customization. |

---

## ✨ Key Features

- 🎨 **Modern UI with Persian Font Support:** Uses `BMitra` font for correct and beautiful Persian text rendering.
- 🎧 **Comprehensive Multi-Media Archive:**
  - **Podcasts (AudioWork):** Audio files with topic categorization.
  - **Videos (VideoWork):** Educational videos and lectures.
  - **Books (Book):** PDF/EPUB files with cover images.
  - **Articles (TextWork):** Textual and PDF research content.
- 🔍 **Advanced Search:** Search across all content types (title, description, categories).
- 📂 **Intelligent Categorization:** Organize content by topic (Psychology, Therapy, Self-Help, Mindfulness, etc.).
- 🎬 **Dynamic Slider:** Highlight important or new items on the homepage with clickable links.
- 📄 **Dynamic Pages:**
  - **About Us:** Dr. Kaman's bio, editable via the admin panel.
  - **Contact Us:** Contact form submitted directly to the admin.
- 🛡 **Security & Validation:**
  - File format validation (only PDF, EPUB, MP3, WAV, JPG, PNG allowed).
  - Automatic media file management in designated folders.
- 🌐 **Responsive Design:** Displays correctly on mobile, tablet, and desktop.

---

## 📥 Installation & Setup

### 1. For General Users (Live Website)
*The live website link is currently pending deployment on VPS YTA 2.*

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

---

## 🛠 Tech Stack

| Technology | Role |
|------------|------|
| **Django 4.2+** | Main Web Framework (MVC Pattern) |
| **Python 3.10+** | Programming Language |
| **SQLite** | Default Database (Configurable to PostgreSQL for Production) |
| **Pillow** | Image Processing (for book covers and sliders) |
| **BMitra Font** | Professional Persian typography |
| **HTML5/CSS3** | Frontend Templates |

---

## 📸 Screenshots

*Since real screenshots are not yet available, here is a text overview of the layout:*

- **Homepage:** Dynamic slider highlighting key content + quick links to categories.
- **Content Gallery:** Clean card-based layout for podcasts, videos, books, and articles with filtering options.
- **Search Interface:** Advanced search form allowing queries across titles, descriptions, and content bodies.

---

## 📝 Project Structure

```
dr-kaman-site/
├── assets/                  # Graphics and screenshots
├── audios/                  # Podcast app
│   ├── models.py, views.py, urls.py
├── books/                   # Book app
├── categories/              # Content categorization
├── core/                    # Main app (slider, about, contact)
├── search/                  # Custom search engine
├── static/                  # Static files (CSS, JS, Fonts)
├── templates/               # HTML templates
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
*Maintained by Mohammad Hasan Kaman | Last updated: July 2026*

> **Disclaimer:** This project is designed for educational and archival purposes only. All content belongs to Dr. Mohammad Reza Kaman.