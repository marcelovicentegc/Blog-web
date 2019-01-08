from mysite.settings.base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration





with open('/var/www/marcelo.page/sensitive/sentry_dsn.txt') as f:
    SENTRY_DSN = f.read().strip()

sentry_sdk.init(
    dsn='https://530276f18aa14d7fb534a9652f49808e@sentry.io/1305425',
    integrations=[DjangoIntegration()]
)

DEBUG = False

with open('/var/www/marcelo.page/sensitive/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
    
with open('/var/www/marcelo.page/sensitive/db_page_name.txt') as f:
    DB_PAGE_NAME = f.read().strip()

with open('/var/www/marcelo.page/sensitive/db_page_user.txt') as f:
    DB_PAGE_USER = f.read().strip()

with open('/var/www/marcelo.page/sensitive/db_page_password.txt') as f:
    DB_PAGE_PASSWORD = f.read().strip()
    
ALLOWED_HOSTS = ['marcelo.page', 'www.marcelo.page', '198.199.69.102']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_PAGE_NAME,
        'USER': DB_PAGE_USER,
        'PASSWORD': DB_PAGE_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = '/var/www/marcelo.page/static/'
MEDIA_ROOT = '/var/www/marcelo.page/media/'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 63072000
X_FRAME_OPTIONS = 'DENY' 