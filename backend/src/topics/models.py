from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Topic(Base):
    __tablename__ = 'topics'

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('topic_categories.id'), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    telegram_name: Mapped[str] = mapped_column(nullable=False)


class TopicCategory(Base):
    __tablename__ = "topic_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

