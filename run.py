from os import path

PWD = path.dirname(__file__)

from sys import path
path.append(PWD)

import pretty_html

pretty_html.app.run()
