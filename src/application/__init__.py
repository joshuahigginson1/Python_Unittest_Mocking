# Imports --------------------------------------------------------------

from flask import Flask

# Configure App --------------------------------------------------------

app = Flask(__name__)

from application import routes
