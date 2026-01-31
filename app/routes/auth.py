from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import LoginForm
from werkzeug.security import check_password_hash
from flask_login import login_user

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash("Welcome back, {0}!".format(user.username), "success")
            redirect_url = request.args.get("next") or url_for("portfolio.index")
            return redirect(redirect_url)
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)
