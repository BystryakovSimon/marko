# -*- coding: utf-8 -*-
import os
import sys

PROJECT_PATH = os.path.normpath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_PATH, 'apps'))
sys.path.append(os.path.join(PROJECT_PATH, '..\\apps'))

PROJECT_ROOT = os.path.abspath('%s/../' % os.path.dirname(__file__))

gettext = lambda s: s

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Semen', 'bistrikovsemen@gmail.com'),
)

ADMIN_TOOLS_INDEX_DASHBOARD = 'settings.dashboard.CustomIndexDashboard'


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_PATH, 'marko.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGES = (
    ('ru', gettext('Russia')),
)

LANGUAGE_CODE = 'ru-RU'

USE_I18N = True

USE_L10N = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
#USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.


# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(PROJECT_ROOT, "/static")
STATIC_URL = "/static/"

ADMIN_MEDIA_PREFIX = STATIC_ROOT + 'admin/'

DATE_FORMAT = "j.m.Y"
DATETIME_FORMAT = "j.m.Y G:i"
TIME_FORMAT = "G:i"
SHORT_DATETIME_FORMAT = "j.m.Y G:i"

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yh99gqikg@0e^(*0(=k_&amp;a!q!yws99=5w^zfy36oh*s#48aw#j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',

    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',

    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware'
)

ROOT_URLCONF = 'settings.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'settings.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

CMS_TEMPLATES = (
    ('contentandgallery.html', u'Текст и галерея'),
    ('mixerscarusel.html'    , u'Карусель смесителей'),
    ('sinkscarusel.html'     , u'Карусель моек'),
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',

    'django',

    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cms.plugins.teaser',
    'cms.plugins.video',
    'cms.plugins.twitter',
    'cms.plugins.inherit',

    'mptt',
    'publisher',
    'menus',

    'form_designer',
    'form_designer.contrib.cms_plugins.form_designer_form',

    'classytags',
    'html5lib',
    'sekizai',
#    'filer',

#    'south',

    'lib',
    'gallerycolors',
    'gallerycountertops',
    'gallerysink',
    'gallerymixers',
)

CMS_PLACEHOLDER_CONF = {
    'footer': {
        'plugins': (),
        'extra_context': {"theme":"wide"},
        'name': gettext(u"Футер")
    },
    'content': {
        'plugins': (),
        'extra_context': {"theme":"wide"},
        'name': gettext(u"Контент")
    },
    'carusel': {
        'plugins': (),
        'extra_context': {"theme":"wide"},
        'name': gettext(u"Карусель")
    },
    'gallery': {
        'plugins': (),
        'extra_context': {"theme":"wide"},
        'name': gettext(u"Галерея")
    },
    'contentimg': {
        'plugins': (),
        'extra_context': {"theme":"wide"},
        'name': gettext(u"Картинка в тексте")
    },
    'contenttitle': {
        'plugins': (),
        'extra_context': {"theme":"wide"},
        'name': gettext(u"Заголовок текста")
    },
    'picture': {
        'plugins': (),
        'extra_context': {"theme":"wide"},
        'name': gettext(u"Картинка в тексте")
    },
}

ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"