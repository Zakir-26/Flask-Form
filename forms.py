from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class myForm(FlaskForm):
    name = StringField("Full Name:", validators=[DataRequired(), Length(max=20)])
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=6, max=16)])
    submit = SubmitField("Register")


if __name__ == "main":
    app.run(debug = True)