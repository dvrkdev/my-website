from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash

from app.forms import LoginForm
from app.models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("portfolio.index"))
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
    return render_template("auth/login.html", form=form)
