import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '.', 'site-packages'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "djsqsq.settings")

import sae
from djsqsq import wsgi

application = sae.create_wsgi_app(wsgi.application)