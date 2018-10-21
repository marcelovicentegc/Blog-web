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
