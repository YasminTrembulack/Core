from uuid import UUID

from sqlalchemy.orm import Session

from models.user_unit import UserUnit


class UserUnitRepository:
    
    def __init__(self, db: Session):
        self._db = db
        
    def create_user_unit(self, user_id: UUID, unit_id: str):
        relation = UserUnit(
            user_id=user_id,
            unit_id=unit_id
        )

        self._db.add(relation)
        self._db.commit()
        self._db.refresh(relation)

        return relation


    def get_user_units(self, user_id: UUID):
        return (
            self._db.query(UserUnit)
            .filter(UserUnit.user_id == user_id)
            .all()
        )
