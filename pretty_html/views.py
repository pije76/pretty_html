from pretty_html import app
from flask import render_template

from .forms import HtmlPrettify


@app.route("/")
def index():
    form = HtmlPrettify()
    return render_template("index.html", form=form)
