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

    def validate_email(self, email):
        if "@" in email.data:
            ait = email.data.split("@")[1]
        else:
            raise ValidationError("Enter valid email.")

        if (
            "_" not in email.data.split("@")[0]
            or len(email.data.split("@")[0].split("_")[1]) != 5
        ):
            raise ValidationError("Enter valid email.")

        if ait != "aitpune.edu.in":
            raise ValidationError("Only @aitpune.edu.in email address allowed.")

    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Create Account")

    def validate_email(self, email):
        try:
            pass
            # user = auth.get_user_by_email(email.data)
        except Exception as e:
            user = False

        if user:
            raise ValidationError("That email is taken. Please choose a different one.")

        if "@" in email.data:
            ait = email.data.split("@")[1]
        else:
            raise ValidationError("Enter valid email.")

        if (
            "_" not in email.data.split("@")[0]
            or len(email.data.split("@")[0].split("_")[1]) != 5
        ):
            raise ValidationError("Enter valid email.")

        if ait != "aitpune.edu.in":
            raise ValidationError("Only @aitpune.edu.in email address allowed.")
