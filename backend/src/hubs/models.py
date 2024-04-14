from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db.db import Base


class Company(Base):
    __tablename__ = 'companies'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey('companies.id'), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    subjects: Mapped[str] = mapped_column(nullable=False)
    level: Mapped[str] = mapped_column(nullable=False)

