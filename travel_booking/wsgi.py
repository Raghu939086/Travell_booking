import os
import sys

# Project root directory containing manage.py
project_home = '/home/gajamraghu/Travell_booking'  
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Use the exact project module name for settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_booking.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
