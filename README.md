# Quality Watch Website

A Django-based web application for browsing, filtering, and managing a catalog of watches. The site supports user registration, login, product browsing by category and style, and a contact form. It is designed for a business selling various types of watches, with an admin panel for management.

## Features

- User registration and login
- Browse watches by category (Kids, Ladies, Mens) and style (Professional, Trendy, Luxury, Elegant, Sports, Smart)
- Product catalog with images, descriptions, and stock info
- Contact form for customer inquiries
- Admin panel (with Jazzmin theme) for managing products, brands, and customers
- Responsive HTML templates for all main pages

## Project Structure

```
project1/
├── manage.py
├── db.sqlite3 (or MySQL)
├── watch/           # Main Django app
│   ├── models.py    # Data models: Customer, Brand, Products, Contactus
│   ├── views.py     # Main views for product browsing, auth, contact, etc.
│   ├── urls.py      # App URL routes
│   └── ...
├── project1/        # Django project config
│   ├── settings.py  # Settings (uses MySQL by default)
│   └── ...
├── static/          # Static files (img, js, css)
├── templates/
│   └── watch/       # HTML templates for all pages
└── ...
```

## Requirements

- Python 3.8+
- Django 5.2
- django-jazzmin 3.0.1
- mysqlclient 2.2.7
- pillow 11.2.1

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/philips8275/Quality_Watch_website.git
   cd Quality_Watch_website/
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install manually:
   ```bash
   pip install Django==5.2 django-jazzmin==3.0.1 mysqlclient==2.2.7 pillow==11.2.1
   ```
4. **Configure the database:**
   - By default, the project uses MySQL. Update `DATABASES` in `project1/settings.py` with your MySQL credentials.
   - To use SQLite for testing, replace the `DATABASES` config with:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
     ```
5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

- Visit `http://127.0.0.1:8000/` to access the home page.
- Use the navigation to browse products by category or style.
- Register or log in to access personalized features.
- Use the contact form for inquiries.
- Admin panel: `http://127.0.0.1:8000/admin/` (login with superuser credentials).

## Main URLs

- `/` - Home
- `/product/` - Product catalog
- `/about/` - About page
- `/contact/` - Contact form
- `/login/` - User login
- `/signup/` - User registration
- `/admin/` - Admin panel
- `/kids/`, `/ladies/`, `/mens/`, `/trendy/`, `/professional/`, `/elegant/`, `/sports/`, `/smart/`, `/luxuary/`, `/catalog/` - Product filters

## Templates

All HTML templates are in `project1/templates/watch/`:
- `home.html`, `index.html`, `product.html`, `about.html`, `contact.html`, `login.html`, `signup.html`, `catalog.html`, etc.

## Static & Media Files

- Static files: `project1/static/`
- Uploaded images: `project1/media/`

## Admin Panel

- Enhanced with [Jazzmin](https://django-jazzmin.readthedocs.io/) for a modern UI.
- Manage products, brands, and customers.

## License

This project is for educational/demo purposes. Please update with your own license as needed. 