from .base import *
import dj_database_url
from decouple import config


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['iris-energy.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# lOGGING SYSTEM
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, 
    'formatters':{
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'Simple_Format':{
            'format': '{levelname} {message}',
            'style': '{',
        }
    },
 
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
            # 'class': 'logging.FileHandler',
            # 'filename': './logs/log_file1.log',
            'formatter':'Simple_Format',
        },
 
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
 
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },

}

DEBUG_PROPAGATE_EXCEPTIONS = True