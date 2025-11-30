import os, django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.core.management import call_command
call_command('collectstatic', '--noinput', '--clear')