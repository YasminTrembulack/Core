from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database.connection import get_db
from services.user_service import UserService

router = APIRouter()

class UserCreate(BaseModel):
    phone: str = Field(..., description="Número de telefone com DDD", example="5511999999999")
    first_name: str | None = None
    last_name: str | None = None


@router.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    
    return service.create_user_if_not_exists(
        first_name=payload.first_name,
        last_name=payload.last_name,
        phone=payload.phone,
    )