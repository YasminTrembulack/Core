import uuid

from sqlalchemy import String, Boolean, Text, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    first_name: Mapped[str | None] = mapped_column(String(100))

    last_name: Mapped[str | None] = mapped_column(String(100))

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    last_message: Mapped[str | None] = mapped_column(Text)

    last_message_at: Mapped[str | None] = mapped_column(TIMESTAMP)

    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"))
