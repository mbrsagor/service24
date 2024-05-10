import os
import stripe
import environ
from django.utils.translation import gettext_lazy as _
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=list,
)

envfile_path = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(envfile_path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_auth',
    'corsheaders',
    'rest_framework',
    'django_filters',
    # 'rest_framework_material',
    'rest_framework.authtoken',
]

LOCAL_APPS = [
    'core',
    'user',
    'service',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Language translate
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'service24.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'service24.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('es', _('Spanish')),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MongoDB configuration.
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': env("DB_NAME"),
        'host': env("DB_HOST"),
        'port': env("DB_PORT")
    }
}

# Django Message Framework
MESSAGE_TAGS = {
    messages.ERROR: 'ERROR',
    messages.INFO: 'SUCCESS',
    messages.WARNING: 'WARNING'
}

# Django auth user info
LOGIN_URL = 'login/'
LOGIN_REDIRECT_URL = 'login/'
AUTH_USER_MODEL = 'user.User'
AUTHENTICATION_BACKENDS = ["user.backend.AuthenticationBackend"]

# Mail sending using SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')

# Django REST framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 8,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

CORS_ORIGIN_ALLOW_ALL = False

# we whitelist localhost:3000 because that's where frontend will be served
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000'
]

HOST_URL = 'http://127.0.0.1:8000/'

# Allow upload big file
MAX_UPLOADING_FILE_SIZE = 31457280  # 30 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 512545
FILE_UPLOAD_MAX_MEMORY_SIZE = 512545
