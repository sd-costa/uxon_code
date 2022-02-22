#!/var/www/uxon/env/bin/python

APP_ROOT = '/var/www/uxon/'

import sys, os
sys.path.insert(0, APP_ROOT)


#import flask
#from app import app
#application = app()

from app import app as application
