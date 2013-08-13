import os

from .base import *

if os.path.exists(os.path.join(os.path.dirname(__file__), 'local.py')):
    try:
        from .local import *
    except:
        pass
