from logger import logger

from sqlalchemy.orm import Session

from models.alarm import AlarmStatus
from repository.alarm_repository import AlarmRepository
from services.galileo_service import GalileoService


class AlarmService:

    def __init__(self, db: Session):
        self.repository = AlarmRepository(db)
        self.galileo_service = GalileoService()

    def create_alarm_if_not_exists(self, alarm_id: str, status: AlarmStatus = AlarmStatus.PENDING):
        return self.repository.create_alarm(
            alarm_id=alarm_id,
            status=status
        )
    
    def get_new_alarms(self):
        current_alarms = self.galileo_service.get_alarms()

        if isinstance(current_alarms, dict):
            current_alarms = [current_alarms]
            
        if not isinstance(current_alarms, list):
            logger.error(f"Expected a list of alarms, but got: {type(current_alarms)}")
            return []
            
        new_alarms = []
        
        for alarm in current_alarms:
            if not isinstance(alarm, dict):
                logger.warning(f"Skipping invalid alarm item type: {type(alarm)}")
                continue
                
            alarm_id = str(alarm.get("alarmeId"))
            if not alarm_id or alarm_id == "None":
                continue

            alarm_found = self.repository.find_by_alarm_id(alarm_id)
            
            if alarm_found is not None:
                if alarm_found.status != AlarmStatus.PENDING:
                    continue

            new_alarms.append(alarm)
        
        return new_alarms