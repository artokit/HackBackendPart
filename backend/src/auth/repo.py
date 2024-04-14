from typing import Optional
from sqlalchemy import insert, select
from .roles import Roles
from .schemas import UserRegister
from .models import User
from .utils import hash_password
from db.db import async_session_maker


async def add_user(user_register: UserRegister) -> User:
    async with async_session_maker() as session:
        stmt = insert(User).values(
            email=user_register.email,
            hashed_password=hash_password(user_register.password).decode(),
            full_name=user_register.full_name,
            telegram_user=user_register.telegram_user,
            role=Roles.USER.value
        ).returning(User)
        res = await session.execute(stmt)
        await session.commit()
        return res.fetchone()[0]


async def exist_telegram_user(telegram_user: str) -> bool:
    async with async_session_maker() as session:
        stmt = select(User).where(User.telegram_user == telegram_user)
        res = await session.execute(stmt)
        return not not res.fetchone()


async def exist_email(email: str) -> bool:
    async with async_session_maker() as session:
        stmt = select(User).where(User.email == email)
        res = await session.execute(stmt)
        return not not res.fetchone()


async def get_user_by_email(email: str) -> User:
    async with async_session_maker() as session:
        stmt = select(User).where(User.email == email)
        res: User = (await session.execute(stmt)).fetchone()

        if res is not None:
            return res[0]


async def get_user_by_id(id: int) -> Optional[User]:
    async with async_session_maker() as session:
        stmt = select(User).where(User.id == id)
        res: User = (await session.execute(stmt)).fetchone()

        if res is not None:
            return res[0]
