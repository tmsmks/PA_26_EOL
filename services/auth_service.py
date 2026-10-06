"""Comptes : validation, inscription, authentification.

Mots de passe hachés par Werkzeug (scrypt). Si `REGISTRATION_CODE` est défini,
l'inscription exige ce code (utile quand l'application est exposée en ligne).
"""
from __future__ import annotations

import hmac
import re

from werkzeug.security import check_password_hash, generate_password_hash

from repositories.orm import ROLE_PARTICIPANT, User
from repositories.users import UserRepository

USERNAME_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{2,39}$")
MIN_PASSWORD = 8
MAX_PASSWORD = 200
MAX_DISPLAY_NAME = 80

# Hash factice : même coût de vérification que l'utilisateur existe ou non.
_DUMMY_HASH = generate_password_hash("dummy-password-for-timing")


class AuthError(ValueError):
    """Saisie refusée ; le message est affichable tel quel."""


def normalize_username(username: str) -> str:
    return (username or "").strip().lower()


def validate_password(password: str) -> None:
    if len(password or "") < MIN_PASSWORD:
        raise AuthError(f"Le mot de passe doit contenir au moins {MIN_PASSWORD} caractères.")
    if len(password) > MAX_PASSWORD:
        raise AuthError("Mot de passe trop long.")


def hash_password(password: str) -> str:
    return generate_password_hash(password)


def register(
    users: UserRepository,
    username: str,
    password: str,
    display_name: str = "",
    role: str = ROLE_PARTICIPANT,
    registration_code: str | None = None,
    expected_code: str | None = None,
) -> User:
    if expected_code and not hmac.compare_digest(
        (registration_code or "").strip().encode(), expected_code.encode()
    ):
        raise AuthError("Code d'inscription incorrect.")
    username = normalize_username(username)
    if not USERNAME_RE.match(username):
        raise AuthError(
            "Identifiant : 3 à 40 caractères, lettres minuscules, chiffres, « . », « _ » ou « - »."
        )
    validate_password(password)
    if users.get_by_username(username) is not None:
        raise AuthError("Cet identifiant est déjà utilisé.")
    name = " ".join((display_name or "").split())[:MAX_DISPLAY_NAME] or username
    return users.create(username, name, hash_password(password), role)


def authenticate(users: UserRepository, username: str, password: str) -> User | None:
    user = users.get_by_username(normalize_username(username))
    if user is None:
        check_password_hash(_DUMMY_HASH, password or "")
        return None
    if not check_password_hash(user.password_hash, password or ""):
        return None
    return user
