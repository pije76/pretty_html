from pretty_html import app
from flask import render_template, redirect
from bs4 import BeautifulSoup

from .forms import HtmlPrettify


@app.route("/", methods=["GET"])
def index():
    form = HtmlPrettify()
    return render_template("index.html", form=form)


@app.route("/result", methods=["GET", "POST"])
def result():
    form = HtmlPrettify()
    if form.validate_on_submit():
        data = form.data
        html = BeautifulSoup(data['html'].encode('utf-8'))
        pretty_html = html.prettify(formatter="html")
        return render_template("result.html", pretty_html=pretty_html)

    return redirect('/')
