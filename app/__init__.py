""" Creates instance of Flask class (named `app`)

`__name__` is the name of the module it is used in

The `routes` module needs to import the `app` variable. So `app` needs to be defined before `routes` is
imported from it.
"""

from flask import Flask

app = Flask(__name__)

from app import routes
