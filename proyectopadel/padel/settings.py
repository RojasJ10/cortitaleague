#encoding:utf-8
import os
RUTA_PROYECTO = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^q8^cd7)pq@jw7n+@ssm(zyt&(!cd+nlha=@8_%q3s9e3f6m5n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'principal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'padel.urls'

WSGI_APPLICATION = 'padel.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(RUTA_PROYECTO, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Admin
ADMINS = (
('Jose Rojas', 'i92roarj@uco.es'),
)

#Templates

RUTA_PROYECTO2 = os.path.dirname(__file__)

TEMPLATE_DIRS = ( os.path.join(RUTA_PROYECTO2, 'plantillas'),)

#Images

MEDIA_ROOT = os.path.join(RUTA_PROYECTO2,'carga')

MEDIA_URL = 'http://127.0.0.1:8000/media/'  #Importante esta linea para ver las imagenes en el explorador

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#STATIC_ROOT = os.path.join(RUTA_PROYECTO2,'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
os.path.join(RUTA_PROYECTO2,'static'),
)
