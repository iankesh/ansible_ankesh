activate_this = '/var/www/demo/.venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
os.environ['DATABASE_URI'] = 'mysql://demo:demo@35.160.137.35/demo'

import sys
sys.path.insert(0, '/var/www/demo')

from demo import app as application
