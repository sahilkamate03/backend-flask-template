# Write Forms Here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    TextAreaField,
    RadioField,
    SelectField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
    InputRequired,
)
from core.models import Users


class UserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    phone_number = StringField(
        "Phone Number", validators=[DataRequired(), Length(max=15)]
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(max=255)])
    role = SelectField(
        "Role",
        choices=[("seller", "Seller"), ("buyer", "Buyer")],
        validators=[DataRequired()],
    )


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    phone_number = StringField(
        "Phone Number", validators=[DataRequired(), Length(max=15)]
    )
    role = SelectField(
        "Role",
        choices=[("buyer", "Buyer"), ("seller", "Seller")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Create Account")

    def validate_email(self, email):
        try:
            user = Users.query.filter_by(
                email=email.data
            ).first()  # Query the user by email
        except Exception as e:
            user = False

        if user:
            raise ValidationError("That email is taken. Please choose a different one.")

        if "@" in email.data:
            ait = email.data.split("@")[1]
        else:
            raise ValidationError("Enter valid email.")
