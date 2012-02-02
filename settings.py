# Django settings for Factivity project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('First Last', 'email@somewhere.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'factivity'             # Or path to database file if using sqlite3.
DATABASE_USER = 'factivity'             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/factivity/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4+a88$=hockdj#de(g=fg#vs*1avs+swc#89czbkbh3l%n@*xr'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'Factivity.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/raid0/projects/django/Factivity/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'Factivity.annual'
)

# for login stuff
SESSION_COOKIE_NAME   = 'factivity_session'
LOGIN_URL = '/factivity/login'
LOGIN_REDIRECT_URL = '/factivity/'
AUTHENTICATION_BACKENDS = ('Factivity.annual.auth.ActiveDirectoryBackend',)

### ACTIVE DIRECTORY SETTINGS

# AD_DNS_NAME should set to the AD DNS name of the domain (ie; example.com)  
# If you are not using the AD server as your DNS, it can also be set to 
# FQDN or IP of the AD server.

AD_DNS_NAME = 'example.com'
AD_LDAP_PORT = 389

AD_SEARCH_DN = 'OU=SOMETHING'

# This is the NT4/Samba domain name
AD_NT4_DOMAIN = 'SOME_DOMAIN'

AD_SEARCH_FIELDS = ['mail','givenName','sn','sAMAccountName']

AD_LDAP_URL = 'ldap://%s:%s' % (AD_DNS_NAME,AD_LDAP_PORT)
