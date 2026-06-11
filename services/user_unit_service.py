from uuid import UUID

from sqlalchemy.orm import Session

from repository.user_unit_repository import UserUnitRepository
from services.galileo_service import GalileoService


class UserUnitService:

    def __init__(self, db: Session):
        self.repository = UserUnitRepository(db)
        self.galileo_service = GalileoService()

    def create_user_unit(self, user_id: UUID, unit_id: str):
        return self.repository.create_user_unit(user_id=user_id, unit_id=unit_id)

    def get_units_from_user(self, user_id: UUID):
        user_units = self.repository.get_user_units_by_user_id(user_id=user_id)
        
        units_ids = set([uu.unit_id for uu in user_units])
        
        return self.galileo_service.get_unit_by_ids(units_ids)
    
    def get_users_from_unit(self, unit_id: int):
        return self.repository.get_user_units_by_unit_id(unit_id=unit_id)
