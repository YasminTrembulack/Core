from uuid import UUID

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.connection import get_db
from services.user_unit_service import UserUnitService

router = APIRouter()

class UserUnitCreate(BaseModel):
    user_id: UUID
    unit_id: str

@router.post("/user-unit", status_code=status.HTTP_201_CREATED)
def create_user_unit(payload: UserUnitCreate, db: Session = Depends(get_db)):
    service = UserUnitService(db)

    return service.create_user_unit(
        user_id=payload.user_id,
        unit_id=payload.unit_id
    )


@router.get("/user-unit/user/{user_id}")
def get_user_units_by_user_id(user_id: UUID, db: Session = Depends(get_db)):
    service = UserUnitService(db)

    return service.get_units_from_user(user_id)

@router.get("/user-unit/unit/{unit_id}")
def get_user_units_by_unit_id(unit_id: str, db: Session = Depends(get_db)):
    service = UserUnitService(db)

    return service.get_users_from_unit(unit_id)
