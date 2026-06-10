from uuid import UUID

from sqlalchemy.orm import Session

from models.alarm import AlarmStatus
from repository.alarm_repository import AlarmRepository
from services.galileo_service import GalileoService


class AlarmService:

    def __init__(self, db: Session):
        self.repository = AlarmRepository(db)
        self.galileo_service = GalileoService()

    def create_alarm_if_not_exists(self, alarm_id: str, status: AlarmStatus = AlarmStatus.PENDING):
        existing_alarm = self.repository.find_by_alarm_id(alarm_id)

        if existing_alarm:
            return existing_alarm

        return self.repository.create_alarm(
            alarm_id=alarm_id,
            status=status
        )
    
    def get_new_alarms(self):
        current_alarms = self.galileo_service.get_alarms()
        
        new_alarms = []
        
        for alarm in current_alarms:
            alarm_id = str(alarm["alarmeId"])
            alarm_found = self.repository.find_by_alarm_id(alarm_id)
            
            if alarm_found is not None:
                if alarm_found.status != AlarmStatus.PENDING:
                    continue

            new_alarms.append(alarm)
        
        return new_alarms
