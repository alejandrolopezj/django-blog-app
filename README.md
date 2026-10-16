# Django Blog Course Project

A simple blog web application built with Django and Python.

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1%2B-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tests](https://github.com/alejandrolopezj/django-blog-app/actions/workflows/tests.yml/badge.svg)](https://github.com/alejandrolopezj/django-blog-app/actions/workflows/tests.yml)
[![Test Coverage](https://codecov.io/gh/alejandrolopezj/django-blog-app/branch/main/graph/badge.svg)](https://codecov.io/gh/alejandrolopezj/django-blog-app)

## Overview

This project is a blog platform built as part of a Django course. It allows users to browse blog posts, view post
details, and read/submit comments.

### Key Features

- **Starting / Home Page**: Displays featured/latest blog posts.
- **All Posts**: Browse all published blog posts.
- **Post Detail**: View full blog post content with associated tags, author info, and comments.
- **Comments**: Submit and read comments on blog posts.
- **Admin Panel**: Manage posts, authors, tags, and comments via Django's built-in administration interface.
- **File Uploads**: Supports image uploads for blog posts.

---

## Tech Stack

- **Language**: Python (>= 3.10 recommended)
- **Web Framework**: [Django](https://www.djangoproject.com/) (`>=6.1,<7.0`)
- **Image Processing**: [Pillow](https://python-pillow.org/) (`>=12.3.0,<13.0.0`)
- **Database**: SQLite3 (`db.sqlite3`)
- **Package Manager**: `pip` (standard `requirements.txt`)

---

## Requirements

- Python 3.10+ (or compatible Python 3 version)
- `pip` package manager
- Virtual environment tool (such as standard library `venv`)

---

## Getting Started / Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd django-blog-app
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On macOS/Linux:
   python3 -m venv .venv
   source .venv/bin/activate

   # On Windows:
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Entry Points & Useful Scripts

All standard Django management commands are run through `manage.py`:

- **Run development server**:
  ```bash
  python manage.py runserver
  ```
- **Apply migrations**:
  ```bash
  python manage.py migrate
  ```
- **Create new migrations**:
  ```bash
  python manage.py makemigrations
  ```
- **Run tests**:
  ```bash
  python manage.py test
  ```
- **Create an admin user**:
  ```bash
  python manage.py createsuperuser
  ```
- **Django interactive shell**:
  ```bash
  python manage.py shell
  ```
- **Create demonstration posts**:
  ```bash
  python manage.py seed_posts
  ```
- **Recreate only the demonstration posts**:
  ```bash
  python manage.py seed_posts --reset
  ```

---

## Environment Variables

Currently, configuration settings (such as `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS`) are configured directly in
`my_site/settings.py`.

- TODO: Extract sensitive settings (e.g. `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, database configuration) into
  environment variables using `.env` files (e.g., via `python-dotenv` or `django-environ`) for production deployment.

---

## Testing

Run the Django test suite using:

```bash
python manage.py test
```

Or test the `blog` app specifically:

```bash
python manage.py test blog
```

### Continuous integration and coverage

Every push and pull request runs the Django test suite through GitHub Actions. The workflow also generates a coverage
report and uploads it to [Codecov](https://codecov.io/).

To enable the Codecov upload, add a repository Actions secret named `CODECOV_TOKEN` with the token generated for this
repository in Codecov. The workflow keeps the token out of the source code.

---

## Project Structure

```text
django-blog-app/
├── blog/                      # Blog application
│   ├── migrations/            # Database migration history
│   ├── static/blog/           # App-specific static CSS and images
│   ├── templates/blog/        # Blog HTML templates & partials
│   ├── admin.py               # Django admin configuration
│   ├── apps.py                # App configuration
│   ├── forms.py               # Blog forms (e.g., comments)
│   ├── models.py              # Database models (Post, Tag, Comment, etc.)
│   ├── tests.py               # Test cases
│   ├── urls.py                # App URL routing
│   └── views.py               # Class-based and function views
├── my_site/                   # Django project configuration
│   ├── asgi.py                # ASGI entrypoint
│   ├── settings.py            # Project settings
│   ├── urls.py                # Root URL configuration
│   └── wsgi.py                # WSGI entrypoint
├── static/                    # Global static files (CSS styles)
├── templates/                 # Global templates (e.g., base.html, 404.html)
├── uploads/                   # Media files root (uploaded post images)
├── db.sqlite3                 # Local SQLite database
├── manage.py                  # Django CLI administrative entry point
└── requirements.txt           # Python dependencies
```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Image Credits

<a href="https://unsplash.com/es/ilustraciones/una-persona-tecleando-en-un-portatil-sobre-un-escritorio-TFQIyR8-lDI?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@karacis_studio/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Karacis Studio</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/un-ordenador-antiguo-con-raton-y-teclado-roPGTtmZZ5U?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@tashakostyuk/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Tasha Kostyuk</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/un-portatil-sobre-un-suelo-azul-aNrC8UbXlOI?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@tashakostyuk/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Tasha Kostyuk</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/iconos-abstractos-de-espacios-de-trabajo-con-portatiles-bCNkCpUXe5c?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@tashakostyuk/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Tasha Kostyuk</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/diseno-web-en-diferentes-dispositivos-YIETA5vgvtA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@publicdomainvectors/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Public domain vectors</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/aparece-una-ciudad-en-un-telefono-de-tablero-de-ajedrez-W_a-1en5dPk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@sashalend/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sasha Lend</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/una-mano-robotica-senala-hacia-la-derecha-4hIiBgBG8Rs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@publicdomainvectors/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Public domain vectors</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/placa-de-circuito-digital-abstracta-con-lineas-rojas-ygxlQaDvZ-c?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@publicdomainvectors/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Public domain vectors</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/puertos-de-ordenador-hdmi-ethernet-y-puertos-usb-iO4QApFb6E4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@tashakostyuk/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Tasha Kostyuk</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/casco-de-realidad-virtual-con-flechas-de-vision-de-360-grados-0Gt1cvp5OVs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@hendi_pe/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Hendi Perkasa</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/portatil-con-memoria-usb-sobre-fondo-verde-0rklfdr33D4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@publicdomainvectors/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Public domain vectors</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

<a href="https://unsplash.com/es/ilustraciones/robot-con-iconos-conectados-para-datos-y-comunicacion-G_0vub80NBc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ilustración</a> de <a href="https://unsplash.com/es/@artgho/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alghozy</a> en <a href="https://unsplash.com/es/ilustraciones?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

---

## Acknowledgments

This project is inspired by the project developed in the [Django course on Udemy](https://www.udemy.com/share/104wQs3@80o6O5ny-X3e_DOqCz7jpfrAJPpym-8Bvr4_XmLeHbm0aM167CGt5bPQSRpwVaaZ/), taught by **Maximilian Schwarzmüller**.
