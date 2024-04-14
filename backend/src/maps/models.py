from sqlalchemy.orm import Mapped, mapped_column
from db.db import Base


class Dot(Base):
    __tablename__ = "dots"

    name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    x: Mapped[int] = mapped_column(nullable=False)
    y: Mapped[int] = mapped_column(nullable=False)
    dots: Mapped[str] = mapped_column(nullable=True)
