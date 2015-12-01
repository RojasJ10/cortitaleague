#encoding:utf-8
import os

RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = 'lhpaujk^5&jw1xyd*@w-9@ei5(enco-#vvguk7gm-&0nj2x@!2'

DEBUG = True

ALLOWED_HOSTS = []


ADMINS = (
    ('Jose Rojas', 'i92roarj@uco.es'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.sites',
    'principal',
    'usuarios',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'topleague.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(RUTA_PROYECTO, 'plantillas')],
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

TEMPLATE_DIRS= (
    os.path.join(RUTA_PROYECTO,'plantillas'),
)

WSGI_APPLICATION = 'topleague.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'topleague.db',
        'USER':'',
        'PASSWORD':'',
        'HOST':'',
        'PORT':'',
    }
}

# Internationalization
LANGUAGE_CODE = 'es-Es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

LOGIN_URL = '/usuarios/login/'

LOGOUT_URL = '/usuarios/logout/'
