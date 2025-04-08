#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import ssl
import socketserver
from http.server import HTTPServer
from django.core.management.commands.runserver import Command as runserver


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# Ensure the SSL configuration is applied correctly
from django.core.management.commands.runserver import Command as runserver

class Command(runserver):
    def get_handler(self, *args, **options):
        handler = super().get_handler(*args, **options)
        self.httpd.socket = ssl.wrap_socket(
            self.httpd.socket,
            certfile='octofit-tracker/backend/ssl.crt',
            keyfile='octofit-tracker/backend/ssl.key',
            server_side=True
        )
        return handler


if __name__ == "__main__":
    main()
