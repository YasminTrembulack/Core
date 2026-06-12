from sqlalchemy import insert
from sqlalchemy.orm import Session

from models.alarm import Alarm, AlarmStatus


class AlarmRepository:
    
    def __init__(self, db: Session):
        self._db = db
        
    def create_alarm(self, alarm_id: str, status: AlarmStatus):
        stmt = insert(Alarm).values(
            alarm_id=alarm_id,
            status=status
        ).on_conflict_do_nothing(
            index_elements=["alarm_id"]
        ).returning(Alarm)

        result = self._db.execute(stmt)
        self._db.commit()

        return result.fetchone()

    def find_by_alarm_id(self, alarm_id: str):
        return (
            self._db.query(Alarm)
            .filter(Alarm.alarm_id == alarm_id)
            .first()
        )
