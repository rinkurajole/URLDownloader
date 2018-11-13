"""
WSGI config for urldownloader project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import sys
import os

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

APPLICATION = get_wsgi_application()
