# عالم الزهور — Flowers World

An informational Arabic website about flowers built with Django.

## Pages

| URL | Page |
|---|---|
| `/` | Home — featured flowers & fun facts |
| `/flowers/` | Encyclopedia — full table with scientific info |
| `/about/` | About the website |
| `/search/` | Search flowers by name, origin, or color |

## Setup

```bash
pip install django
python manage.py migrate
python manage.py loaddata flowers
python manage.py runserver
```

Then open `http://127.0.0.1:8000`
