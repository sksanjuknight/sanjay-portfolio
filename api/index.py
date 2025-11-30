import os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()