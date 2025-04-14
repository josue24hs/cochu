"""
WSGI config for usuarios project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from usuarios.views import hola_mundo


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usuarios.settings')

application = hola_mundo()
