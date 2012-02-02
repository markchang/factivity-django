import os
import sys

sys.path.append('/raid0/projects/django')
sys.path.append('/raid0/projects/django/Factivity')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Factivity.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

