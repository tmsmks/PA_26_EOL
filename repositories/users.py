"""Repository des comptes utilisateurs."""
from __future__ import annotations

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from repositories.orm import ROLE_PARTICIPANT, User, utcnow


class UserRepository:
    def __init__(self, session: Session) -> None:
        self._s = session

    def get(self, user_id: int) -> User | None:
        return self._s.get(User, user_id)

    def get_by_username(self, username: str) -> User | None:
        return self._s.scalar(
            select(User).where(func.lower(User.username) == username.strip().lower())
        )

    def create(
        self,
        username: str,
        display_name: str,
        password_hash: str,
        role: str = ROLE_PARTICIPANT,
    ) -> User:
        user = User(
            username=username,
            display_name=display_name,
            password_hash=password_hash,
            role=role,
        )
        self._s.add(user)
        self._s.commit()
        return user

    def list_all(self) -> list[User]:
        return list(self._s.scalars(select(User).order_by(func.lower(User.display_name))))

    def set_password(self, user: User, password_hash: str) -> None:
        user.password_hash = password_hash
        self._s.commit()

    def set_role(self, user: User, role: str) -> None:
        user.role = role
        self._s.commit()

    def touch_login(self, user: User) -> None:
        user.last_login_at = utcnow()
        self._s.commit()
