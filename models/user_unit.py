import uuid

from sqlalchemy import ForeignKey, TIMESTAMP, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.connection import Base


class UserUnit(Base):
    __tablename__ = "user_units"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    unit_id: Mapped[str] = mapped_column(String(100), nullable=False)

    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    user = relationship("User", back_populates="units", lazy="joined")
