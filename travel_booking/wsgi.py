"""
WSGI config for travel_booking project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import sys
import os

path = '/home/gajamraghu/Travell_booking'  
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Travell_booking.settings'  

activate_this = '/home/gajamraghu/.virtualenvs/travelenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(_file_=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()