# 🧠 Kaman Psychology Portal - Multimedia Archive for Dr. Mohammad Reza Kaman

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![Framework](https://img.shields.io/badge/Django-4.2+-green.svg?logo=django&logoColor=white)](https://djangoproject.com)
[![Database](https://img.shields.io/badge/SQLite-Lightgrey.svg?logo=sqlite&logoColor=orange)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Mohammad-Hasan-Kaman/dr-kaman-site?style=social)](https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site)

> **A comprehensive multimedia archive website for Dr. Mohammad Reza Kaman, featuring an organized collection of psychological lectures, books, articles, and educational content.**  
> Built with ❤️ using **Django**, **SQLite**, and modern web technologies.

---

## ✨ Features

| Feature | Description |
|:---|:---|
| 🎨 **Dynamic Homepage** | Auto-updating slider with latest content and featured categories |
| 🎧 **Audio Archive** | Organized collection of psychological lectures, podcasts, and speeches |
| 📺 **Video Library** | Curated video content from workshops, interviews, and educational sessions |
| 📚 **Book Repository** | Digital and physical book list with detailed descriptions |
| 📝 **Article Archive** | Text-based content including essays, research papers, and blog posts |
| 🗂️ **Smart Categorization** | Hierarchical category system for easy content discovery |
| 🔍 **Advanced Search** | Full-text search across all media types |
| 📱 **Responsive Design** | Mobile-friendly interface for all devices |
| 🛡️ **Dynamic Content Management** | Admin panel to update "About" and "Contact" pages without code changes |
| 🌐 **Persian RTL Support** | Fully localized interface for Persian/Farsi speakers |

---

## 📸 Screenshots

> *Note: Screenshots will be added to `assets/` folder. Running the app once will help capture these.*

| Homepage with Slider | Audio/Video/Books Gallery | Search & Categories |
|:---:|:---:|:---:|
| ![Homepage](assets/screenshot_home.svg) | ![Gallery](assets/screenshot_gallery.svg) | ![Search](assets/screenshot_search.svg) |

*(Placeholders shown - replace with actual screenshots after first run)*

---

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.10+** ([Download](https://python.org/downloads))
- **Git** (optional, for cloning)
- ** pip** (usually included with Python)

### Quick Start
```bash
# 1. Clone the repository
git clone https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site.git
cd dr-kaman-site

# 2. Create a virtual environment (recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
# Copy .env.example to .env and fill in your values (if any)
cp .env.example .env

# 5. Run database migrations
python manage.py migrate

# 6. Create a superuser (admin)
python manage.py createsuperuser

# 7. Collect static files
python manage.py collectstatic

# 8. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the site and `http://127.0.0.1:8000/admin` for the admin panel.

---

## 🏗 Project Structure

```
dr-kaman-site/
├── core/                  # Main application (home, about, contact)
│   ├── models.py          # Slider, AboutPage, ContactPage models
│   ├── views.py           # Home, about, contact views
│   ├── urls.py            # URL routing
│   └── templates/core/    # Home, about, contact templates
├── audios/                # Audio content (lectures, podcasts)
├── videos/                # Video content (workshops, interviews)
├── books/                 # Book repository
├── texts/                 # Articles, essays, research papers
├── categories/            # Content categorization system
├── search/                # Full-text search functionality
├── dr_kaman_site/         # Django project settings
│   ├── settings.py        # Database, apps, middleware config
│   └── urls.py            # Main URL configuration
├── static/                # Global static files (CSS, JS, images)
├── media/                 # User-uploaded media (videos, audios, books)
├── templates/             # Global templates
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (SECRET_KEY, etc.)
└── db.sqlite3             # SQLite database
```

---

## 🎯 Content Types

### 1. Audio Works (`audios`)
- Psychological lectures and speeches
- Podcast episodes
- Meditations and guided sessions

### 2. Video Works (`videos`)
- Workshop recordings
- Interview sessions
- Educational series

### 3. Books (`books`)
- Published books by Dr. Kaman
- Recommended reading list
- Book summaries and reviews

### 4. Text Content (`texts`)
- Articles and essays
- Research papers
- Blog posts

### 5. Categories (`categories`)
- Hierarchical organization
- Tag-based filtering
- Cross-referencing between content types

---

## ⚙️ Configuration

### Environment Variables (`.env`)
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Optional: Database configuration
# DATABASE_URL=postgresql://user:password@localhost:5432/dr_kaman_db
```

### Admin Panel
Access the admin panel at `/admin` to:
- Manage sliders and homepage content
- Add/update audio, video, book, and text content
- Configure categories and search indices
- Update "About" and "Contact" pages dynamically

---

## 🐛 Troubleshooting

| Issue | Solution |
|:---|:---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `sqlite3.OperationalError` | Delete `db.sqlite3` and run `python manage.py migrate` |
| `Static files not found` | Run `python manage.py collectstatic` |
| `ImportError: No module named X` | Check virtual environment activation |
| `Port 8000 already in use` | Use `python manage.py runserver 8001` |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

**Ideas for contribution:**
- Add user authentication and commenting system
- Implement advanced search filters
- Create a newsletter subscription feature
- Add social media sharing buttons
- Improve accessibility (WCAG compliance)

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 About the Project

### Dr. Mohammad Reza Kaman
A renowned psychologist and researcher dedicated to sharing psychological knowledge through multimedia content.

### Developer
**Mohammad Hasan Kaman**  
- 🌐 **GitHub:** [@Mohammad-Hasan-Kaman](https://github.com/Mohammad-Hasan-Kaman)  
- 💼 **LinkedIn:** [Kaman Programmer](https://www.linkedin.com/in/kaman-programmer)  
- 📧 **Email:** [mohammadhasankaman@gmail.com](mailto:mohammadhasankaman@gmail.com)  

I'm a 17-year-old Full-Stack Developer enthusiast passionate about building practical tools that make knowledge accessible to everyone.

---

## ⭐ Support the Project

If you find this archive useful, please **give it a star**! ⭐  
Your support motivates me to keep improving and documenting psychological content.

[![Star History](https://api.star-history.com/svg?repos=Mohammad-Hasan-Kaman/dr-kaman-site&type=Date)](https://star-history.com/#Mohammad-Hasan-Kaman/dr-kaman-site&Date)

---

> **Disclaimer:** This website is a personal archive for educational purposes. All content belongs to Dr. Mohammad Reza Kaman and respective copyright holders.