#!/usr/bin/env python
import os
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_PATH, "apps"))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "billybeez.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
