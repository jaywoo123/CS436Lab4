#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cloud_net.settings")

    import django
    django.setup()

    from django.core.management.commands.runserver import Command as runserver
    runserver.default_addr = "0.0.0.0"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
