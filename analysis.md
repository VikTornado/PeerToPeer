# PeerToPeer Project Analysis

## Overview
PeerToPeer is a Django-based web application designed for an organization to manage its content, news, and volunteer applications. It features a multilingual interface (Ukrainian and English) and a clean, responsive design using Tailwind CSS.

## Architecture

### Backend: Django
- **Django Version**: 4.2.26
- **Database**: PostgreSQL (configured via `dj_database_url`) with SQLite as a fallback for development.
- **Media Storage**: Supports Cloudinary for persistent storage of images and documents.
- **Frontend Assets**: Uses Tailwind CSS, managed via Node.js/NPM.

### Project Structure
- `peertopeer/`: Core project configuration.
- `core/`: Main application logic, including static pages (About, Projects, International, etc.) and volunteer application handling.
- `news/`: News management system with archives and detail views.
- `templates/`: HTML templates using Django Template Language.
- `static/`: Static assets (CSS, images).

## Data Models

### Core App (`core/models.py`)
- **AboutPage**: Stores content for the "About Us" page.
- **ContactPage**: Stores contact information.
- **InternationalPage**: Manages content for "Publications and Publications".
- **ProjectsPage**: Content for "Project Participation".
- **VolunteeringPage**: Content for "Volunteering and Education".
- **StatutPage**: Manages statutory documents, including PDF uploads.

### News App (`news/models.py`)
- **News**: Main model for news articles, including title, content, external links, and a main image.
- **NewsImage**: Supporting model for news galleries.

## Key Features
- **Multilingual Support**: Uses `django-modeltranslation` to provide content in both Ukrainian and English.
- **Rich Text Editing**: Integrated with `django-ckeditor` for easy content management in the admin panel.
- **Volunteer Application Flow**: A custom endpoint `volunteer-apply/` handles JSON applications and sends email notifications.
- **Responsive UI**: Built with Tailwind CSS, ensuring accessibility across devices.

## Running the Project
1.  **Environment**: Recreated the virtual environment and installed dependencies from `requirements.txt`.
2.  **Database**: Ran migrations and populated initial content using `populate_content.py`.
3.  **Server**: Started using `python manage.py runserver 8000`.
4.  **Frontend**: CSS is pre-built in `static/css/styles.css`.
