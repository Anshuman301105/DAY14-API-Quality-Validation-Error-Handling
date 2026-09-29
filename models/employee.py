from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class Employee(Base):

    __tablename__ = "employee"

    employee_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    first_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    last_name: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    phone_number: Mapped[str | None] = mapped_column(
        String(15),
        unique=True,
        nullable=True,
        index=True
    )

    department: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )