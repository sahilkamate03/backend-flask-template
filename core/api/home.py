from flask import Blueprint, render_template, url_for, redirect, request, flash, jsonify
from flask_login import current_user, login_user, logout_user
from core.forms import UserForm, LoginForm
from core.models import Users


home = Blueprint("home", __name__)


@home.route("/")
def home_html():
    return render_template("home.html")


@home.route("/signin")
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("home.home_latest"))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            user_id = 1  # TODO :
        except:
            flash("User not found. Create Account.", "info")
            return redirect(url_for("home.signup"))

        print(user_id.email_verified)
        if email == "admin_18185@aitpune.edu.in":
            pass
        elif not (user_id.email_verified):
            flash("Verify your email.", "info")
            return render_template("./signin.html", title="Login", form=form)

        try:

            user = Users(user_id, email)
            next_page = request.args.get("next")
            login_user(user, remember=form.remember.data)
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("home.home_latest"))
            )
        except Exception as e:
            flash("Login Unsuccessful. Please check email and password", "danger")
            print(e)
            return redirect(url_for("home.signin"))

    return render_template("./signin.html", title="Login", form=form)


@home.route("/signup", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home.home_latest"))
    form = RegistrationForm()
    if form.validate_on_submit():
        print("success")
        email = form.email.data
        password = form.password.data
        role = roleProvider(email)
        data = {
            "name": form.name.data,
            "username": email.split("@")[0],
            "email": email,
            "role": role,
            "add": "-",
            "phone": "-",
            "about": "Write about yourself.",
            "profile_url": "",
            "verified": False,
        }
        try:
            db_fire.collection(role).document(form.email.data.split("@")[0]).set(data)
            auth.create_user(email=email, password=password)
            send_verification_email(email)
            flash(f"Verification link send to email.", "info")
            return redirect(url_for("home.login"))
        except Exception as e:
            print(e)

    return render_template(
        "./auth_page/pages-register.html", title="Register", form=form
    )


@home.route("/api")
def home_latest():
    return jsonify({"message": "Hello Server"})
