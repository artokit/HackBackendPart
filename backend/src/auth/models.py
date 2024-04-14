from sqlalchemy.orm import mapped_column, Mapped

from db.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    full_name: Mapped[str] = mapped_column()
    telegram_user: Mapped[str] = mapped_column(unique=True)
    role: Mapped[str] = mapped_column()
