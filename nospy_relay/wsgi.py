"""
WSGI config for nospy_relay project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nospy_relay.settings')
django.setup()

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
