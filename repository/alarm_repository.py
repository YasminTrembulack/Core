from uuid import UUID

from sqlalchemy.orm import Session

from models.alarm import Alarm, AlarmStatus


class AlarmRepository:
    
    def __init__(self, db: Session):
        self._db = db
        
    def create_alarm(self, alarm_id: str, status: AlarmStatus):
        alarm = Alarm(
            alarm_id=alarm_id,
            status=status
        )

        self._db.add(alarm)
        self._db.commit()
        self._db.refresh(alarm)

    def find_by_alarm_id(self, alarm_id: str):
        return (
            self._db.query(Alarm)
            .filter(Alarm.alarm_id == alarm_id)
            .first()
        )
