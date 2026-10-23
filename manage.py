# NOTE: This file exists only so Vercel can discover the settings module and asgi/wsgi entrypoint.
# NOTE: Use the `djangx` or `djx` command instead of `python manage.py`.
import os
import sys

from djangx.core import DJANGO_SETTINGS_MODULE


def main():
    """Run administrative tasks."""
    assert DJANGO_SETTINGS_MODULE is not None
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
