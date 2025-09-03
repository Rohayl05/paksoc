"""
WSGI config for paksoc project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paksoc.settings')

application = get_wsgi_application()
