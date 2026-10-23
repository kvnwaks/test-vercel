#!/usr/bin/env python
# NOTE: This file exists only so Vercel can discover the settings module and asgi/wsgi entrypoint.
# NOTE: Use the `djangx` or `djx` command instead of `python manage.py`.
# https://vercel.com/docs/frameworks/full-stack/django
import os
import sys

from djangx.core import DJANGO_SETTINGS_MODULE, print_help_message


def main():
    """Run administrative tasks."""
    if DJANGO_SETTINGS_MODULE is not None:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)
    else:
        print_help_message()


if __name__ == "__main__":
    main()
