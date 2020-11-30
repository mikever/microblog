""" Top-level Python script that defines the Flask application instance.

Here we say, from the app package, import that `app` application isntance.

Importing the app package causes `__init__.py` to run, which defines the Flask instance,
and then is imported here.
"""
from app import app

