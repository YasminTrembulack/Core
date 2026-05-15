from uuid import UUID

from fastapi import APIRouter, Depends
from requests import Session

from database.connection import get_db
from services.user_service import UserService

router = APIRouter()

service = UserService()


@router.post("/users")
def create_user(db: Session = Depends(get_db)):
    return

@router.delete("/users/{id}")
def create_user(id: UUID):
    return

@router.post("/users/{user_id}/units/{unit_id}")
def add_unit(user_id: UUID, unit_id: UUID, db: Session = Depends(get_db)):
    return service.link_user_to_unit(
        db=db,
        user_id=user_id,
        unit_id=unit_id
    )

@router.post("/users/{user_id}/units")
def get_user_units(user_id: UUID):
    return service.get_units_from_user(user_id)
