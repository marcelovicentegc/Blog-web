from mysite.settings.base import *




DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_PAGE_NAME'),
        'USER': os.environ.get('DB_PAGE_USER'),
        'PASSWORD': os.environ.get('DB_PAGE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_SECONDS = 0
X_FRAME_OPTIONS = 'SAMEORIGIN'
