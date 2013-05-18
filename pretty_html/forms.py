from flask.ext.wtf import Form, TextAreaField, TextField, Required


class HtmlPrettify(Form):
    html = TextAreaField('HTML', validators=[Required()])
    indentation = TextField('indentation', validators=[Required()], default=4)
