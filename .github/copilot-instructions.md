# PeerToPeer Copilot Instructions

## Project Overview
**PeerToPeer** is a Django-based charitable foundation website with multi-language support (Ukrainian/English). It combines a CMS-like backend (for editable pages) with a news system, using Tailwind CSS for styling and Django i18n for internationalization.

## Architecture & Key Components

### Core Apps
- **`core/`** - Main app handling editable page content (About, Projects, Volunteering, Contact, Statut, International pages) via Django admin
- **`news/`** - News management with support for gallery images per article
- **`peertopeer/`** - Django project settings and URL routing

### Data Flow Patterns
1. **Content Pages**: Use simple `.first()` queries to fetch single-instance content pages (e.g., `AboutPage.objects.first()`) - these are CMS-like pages managed via Django admin
2. **News**: Query-driven (`News.objects.order_by('-created_at')[:3]`) with related `NewsImage` gallery support
3. **Email**: Hardcoded recipient list in views (e.g., `recipient_list = ['info@peertopeer.ua']`) - configure in settings for production

### Internationalization (i18n)
- **Primary language**: Ukrainian (`LANGUAGE_CODE = 'uk'` in settings)
- **Supported languages**: Ukrainian and English
- **Message files**: `locale/{uk,en}/LC_MESSAGES/{django.po,django.mo}`
- **Workflow**: Strings use Django's `{% trans %}` tag in templates; compile with `python manage.py compilemessages`

### Static Assets & Styling
- **Tailwind CSS**: Watch mode via `npm run build:css` (builds `static/css/styles.css`)
- **Theme colors**: Ukrainian flag colors baked into config:
  - Primary: `#0057B8` (blue)
  - Secondary: `#FFD700` (yellow)
- **Typography**: Custom fonts (Inter for body, Montserrat for headings) via Google Fonts
- **Alpine.js**: Lightweight interactivity (included via CDN in `base.html`)

## Critical Developer Workflows

### First-Time Setup
```bash
pip install -r requirements.txt
npm install
python manage.py migrate
python manage.py compilemessages
npm run build:css
```

### Deployment Build (see `build.sh`)
```bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py compilemessages
```

### Running Locally
- **Django dev server**: `python manage.py runserver`
- **CSS watch mode**: `npm run build:css` (in separate terminal)
- **Create superuser**: `python manage.py createsuperuser` → access `/admin/`

### When Adding New Features
- **For editable CMS content**: Add model to `core/models.py` + register in `core/admin.py` + create view + template
- **For news-related**: Use `news/models.py` (News + NewsImage pattern)
- **For i18n strings**: Wrap in `{% trans %}` tags, then run `python manage.py makemessages -l uk -l en` + `compilemessages`
- **For styling**: Edit `static/css/input.css` or use Tailwind classes; rebuild CSS with npm script

## Project-Specific Conventions

### Models & Admin
- All content pages use `RichTextField` from django-ckeditor for admin editing
- CMS content fetched via `.first()` (single-instance assumption)
- Images: `main_image` for News cover, `NewsImage` for galleries with `upload_to='news/'` and `upload_to='news/gallery/'`

### Views
- Most views render a single template with a `page` object context variable
- `volunteer_apply` is the only AJAX endpoint (POST, JSON, returns `{'success': bool, 'message': str}`)
- Email is hardcoded; use Django settings overrides for production

### Templates
- Base extends `base.html` (includes header, footer, i18n support, Open Graph meta)
- Templates organized by app: `core/templates/news/`, `templates/includes/`
- Use `{% load static i18n %}` at top of templates that need assets or translations
- Alpine.js `x-cloak` CSS rule prevents FOUC during load

### Dependencies
- **Backend**: Django 4.2, Pillow (images), django-ckeditor, gunicorn, whitenoise
- **Frontend**: Tailwind CSS 4, PostCSS, Autoprefixer, Alpine.js 3
- **Database**: SQLite (development) - see settings.py for production SMTP/storage setup

## Integration Points & External Systems
- **Email**: Console backend in DEBUG mode; requires SMTP config for production (see `settings.py` comments)
- **Static files**: Served via whitenoise; compressing storage enabled for production
- **Media uploads**: Stored in `media/` (configured in settings), served in DEBUG mode via `django.conf.urls.static`
- **Language switching**: Route `/set-language/` (Django's built-in view) stores preference in session

## Code Style Observations
- English code comments, Ukrainian UI strings and field labels
- Model `__str__` methods return `title` field
- Views use Django's `render()` shortcut
- No explicit error handling in most views (except `volunteer_apply`)
- Admin-driven content management; minimal form validation in frontend
