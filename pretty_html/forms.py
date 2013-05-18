from flask.ext.wtf import Form, TextAreaField, Required


class HtmlPrettify(Form):
    html = TextAreaField('HTML', validators=[Required()])
