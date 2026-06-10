import enum
import uuid

from sqlalchemy import TIMESTAMP, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class AlarmStatus(str, enum.Enum):
    PENDING = "pending"
    NOTIFIED = "notified"
    ACKNOWLEDGED = "acknowledged"
    FAILED = "failed"


class Alarm(Base):
    __tablename__ = "alarms"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    alarm_id: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    status: Mapped[AlarmStatus] = mapped_column(String(50),default=AlarmStatus.PENDING,nullable=False)

    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))