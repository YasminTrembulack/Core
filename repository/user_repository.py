from uuid import UUID

from sqlalchemy.orm import Session

from models.user import User
from models.user_unit import UserUnit


class UserRepository:
    
    def __init__(self, db: Session):
        self._db = db

    def create_user(self, phone: str, first_name: str | None = None, last_name: str | None = None):
        user = User(
            phone=phone,
            first_name=first_name,
            last_name=last_name
        )

        self._db.add(user)
        self._db.commit()
        self._db.refresh(user)

        return user


    def find_by_phone(self, phone: str):
        return (
            self._db.query(User)
            .filter(User.phone == phone)
            .first()
        )
