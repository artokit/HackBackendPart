from sqlalchemy import select, insert, update
from db.db import async_session_maker
from maps.models import Dot
from maps.schemas import Coordinate


async def get_all_destinations():
    async with async_session_maker() as session:
        stmt = select(Dot)
        res = (await session.execute(stmt)).scalars()
        return list({i.name for i in res})


async def add_dot(cord: Coordinate):
    async with async_session_maker() as session:
        await session.execute(insert(Dot).values(x=cord.x, y=cord.y, name=cord.name))
        await session.commit()


async def add_dot_for_debug(x, y, name, nexts):
    async with async_session_maker() as session:
        await session.execute(insert(Dot).values(
            x=int(x),
            y=int(y),
            name=name,
            dots=nexts
        ))
        await session.commit()


async def get_dot(dot_name: str) -> Dot:
    async with async_session_maker() as session:
        res = await session.execute(select(Dot).where(Dot.name == dot_name))
        return res.scalar_one()


async def get_dots():
    async with async_session_maker() as session:
        res = await session.execute(select(Dot))
        return res.scalars().all()


async def add_line(dot_name1: str, dot_name2: str):
    async with async_session_maker() as session:
        dot = await get_dot(dot_name1)
        stmt = update(Dot).values(dots=(dot.dots or "") + f"{dot_name2};").where(Dot.name == dot_name1)
        await session.execute(stmt)
        await session.commit()
