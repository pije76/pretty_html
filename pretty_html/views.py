from pretty_html import app
from flask import render_template, redirect

from .forms import HtmlPrettify


@app.route("/", methods=["GET"])
def index():
    form = HtmlPrettify()
    return render_template("index.html", form=form)


@app.route("/result", methods=["GET", "POST"])
def result():
    form = HtmlPrettify()
    if form.validate_on_submit():
        return render_template("result.html")

    return redirect('/')
