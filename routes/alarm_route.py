
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.connection import get_db
from models.alarm import AlarmStatus
from services.alarm_service import AlarmService

router = APIRouter()

class AlarmCreate(BaseModel):
    alarm_id: int
    status: AlarmStatus

@router.post("/alarm", status_code=status.HTTP_201_CREATED)
def create_alarms(payload: AlarmCreate, db: Session = Depends(get_db)):

    service = AlarmService(db)
    
    return service.create_alarm_if_not_exists(
        alarm_id=str(payload.alarm_id),
        status=payload.status
    )

@router.get("/alarm")
def get_user_units_by_user_id(db: Session = Depends(get_db)):
    service = AlarmService(db)

    return service.get_new_alarms()
