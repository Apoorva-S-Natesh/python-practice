#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_buddy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


"""
Django's command-line utility script. It lets you run commands like:

runserver - start the dev server

migrate - apply database migrations

startapp - create a new app

createsuperuser - make an admin account

run it like: python manage.py runserver

File			What it does
__init__.py		Marks this directory as a Python package.
settings.py		Where you configure your whole project — databases, apps, static files, etc.
urls.py	The 	central URL routing file — maps URLs to views.
asgi.py	Used 	for ASGI deployments (e.g., WebSockets).
wsgi.py	Used 	for WSGI deployments (classic Python web servers).
"""

#superuser password - 123 (/admin)