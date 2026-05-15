from uuid import UUID

from sqlalchemy.orm import Session

from repository.user_repository import UserRepository
from services.galileo_service import GalileoService


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        self.galileo_service = GalileoService()

    def create_user_if_not_exists(self, phone: str, first_name: str | None = None, last_name: str | None = None):
        existing_user = self.repository.find_by_phone(phone)

        if existing_user:
            return existing_user

        return self.repository.create_user(
            phone=phone,
            first_name=first_name,
            last_name=last_name
        )

    def link_user_to_unit(self, user_id: UUID, unit_id: str):
        return self.repository.add_unit_to_user(user_id=user_id, unit_id=unit_id)

    def get_units_from_user(self, user_id: UUID):
        units = self.repository.get_user_units(user_id=user_id)
        
        units_ids = set([u.id for u in units])
        
        return self.galileo_service.get_unit_by_ids(units_ids)