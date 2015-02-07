from .base import *

# http://stackoverflow.com/questions/12771167/django-settings-py-dj-database-url-on-heroku
if os.environ.get('DATABASE_URL'):
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
