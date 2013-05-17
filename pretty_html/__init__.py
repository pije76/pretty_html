from os import path

SETTINGS_PATH = path.dirname(__file__)
PROJECT_PATH = path.dirname(SETTINGS_PATH)
LIBRARIES_PATH = path.join(PROJECT_PATH, 'libraries')

from sys import path
path.append(LIBRARIES_PATH)

from flask import Flask

app = Flask('pretty_html')
app.config.from_object('pretty_html.settings')

from views import *
