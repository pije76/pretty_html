from pretty_html import app
from flask import render_template

from .forms import HtmlPrettify


@app.route("/", methods=["GET", "POST"])
def index():
    form = HtmlPrettify()
    if form.validate_on_submit():
        print "on post"
    return render_template("index.html", form=form)
