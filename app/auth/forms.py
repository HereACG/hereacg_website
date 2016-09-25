from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
import wtforms.vaildators import Required

class LoginForm(Form):
    username = StringField(
        'Username',
        vaildators=[Required()]
        )
    password = PasswordField(
        'Password',
        vaildators=[Required()]
    )
    submit = SubmitField('Login')
