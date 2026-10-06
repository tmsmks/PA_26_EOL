"""Pages de connexion, d'inscription et de déconnexion."""
from __future__ import annotations

from flask import Blueprint, current_app, redirect, render_template, request, url_for

from repositories.database import db_session
from repositories.users import UserRepository
from services.auth_service import AuthError, authenticate, register
from views.guards import current_user, login_user, logout_user, safe_next

auth_bp = Blueprint("auth", __name__)


def _after_login() -> str:
    return safe_next(request.values.get("next")) or url_for("pages.landing")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user() is not None:
        return redirect(_after_login())
    error = None
    username = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        users = UserRepository(db_session())
        user = authenticate(users, username, request.form.get("password", ""))
        if user is not None:
            users.touch_login(user)
            login_user(user)
            return redirect(_after_login())
        error = "Identifiant ou mot de passe incorrect."
    return render_template(
        "auth.html.jinja",
        mode="login",
        error=error,
        username=username,
        next=safe_next(request.values.get("next")),
    ), (401 if error else 200)


@auth_bp.route("/register", methods=["GET", "POST"])
def register_page():
    if current_user() is not None:
        return redirect(_after_login())
    expected_code = current_app.config.get("REGISTRATION_CODE")
    error = None
    form = {"username": "", "display_name": ""}
    if request.method == "POST":
        form = {
            "username": request.form.get("username", ""),
            "display_name": request.form.get("display_name", ""),
        }
        password = request.form.get("password", "")
        try:
            if password != request.form.get("password_confirm", ""):
                raise AuthError("Les deux mots de passe ne correspondent pas.")
            user = register(
                UserRepository(db_session()),
                form["username"],
                password,
                form["display_name"],
                registration_code=request.form.get("registration_code"),
                expected_code=expected_code,
            )
        except AuthError as e:
            error = str(e)
        else:
            login_user(user)
            return redirect(_after_login())
    return render_template(
        "auth.html.jinja",
        mode="register",
        error=error,
        form=form,
        needs_code=bool(expected_code),
        next=safe_next(request.values.get("next")),
    ), (400 if error else 200)


@auth_bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for("pages.landing"))
