"""Vercel reads this for the settings module. For development, run `djangx` or `djx` instead."""

import os
import sys

from djangx.core.utils import DJANGO_SETTINGS_MODULE

assert DJANGO_SETTINGS_MODULE is not None
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

if __name__ == "__main__":
    # Required: Vercel runs `collectstatic` via this file; without it, static assets are skipped.
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
