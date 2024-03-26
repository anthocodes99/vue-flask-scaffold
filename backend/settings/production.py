import os

from .base import *

# NOTE: for sensitive settings, please use environment variables!
# you may also employ Flask's instance folder method instead
# https://flask.palletsprojects.com/en/3.0.x/config/#instance-folders

# ensure that debug mode is not on
DEBUG = False

# different secret key in production for increased security
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', b'e^penxx=uj2zq1p7ao=hale(#fu%iq*)cnfewp*29_eovw$kwc')