from flask.ext.wtf import Form, TextAreaField, Required
from flask.ext.wtf.html5 import IntegerField


class HtmlPrettify(Form):
    html = TextAreaField('HTML', validators=[Required()])
    indentation = IntegerField('indentation', validators=[Required()], default=4)
