from sqlalchemy import insert, select
from hubs.models import Company, Task
from db.db import async_session_maker
from hubs.schemas import AddTask, GetAllTasksByCompany, TaskResponse


async def add_company(name: str) -> Company:
    async with async_session_maker() as session:
        stmt = insert(Company).values(name=name).returning(Company)
        res = await session.execute(stmt)
        await session.commit()
        return (res.fetchone())[0]


async def add_task(task: AddTask) -> Task:
    async with async_session_maker() as session:
        stmt = insert(Task).values(
            company_id=task.company_id,
            title=task.title,
            description=task.description,
            subjects=';'.join(task.subjects),
            level=task.level
        ).returning(Task)
        res = await session.execute(stmt)
        await session.commit()
        return (res.fetchone())[0]


async def get_company_by_id(id) -> Company:
    async with async_session_maker() as session:
        stmt = select(Company).where(Company.id == id)
        res = (await session.execute(stmt)).fetchone()

        if res:
            return res[0]


async def get_all_companies() -> list[Company]:
    async with async_session_maker() as session:
        stmt = select(Company)
        return (await session.scalars(stmt)).all()


async def get_task_by_company_id(company_id: int) -> list[TaskResponse]:
    async with async_session_maker() as session:
        stmt = select(Task).where(Task.company_id == company_id)
        res = (await session.execute(stmt)).scalars()
        return [TaskResponse(id=i.id, title=i.title, description=i.description, subjects=i.subjects.split(";"), level=i.level) for i in res]


async def get_all_task_companies():
    async with async_session_maker() as session:
        stmt = select(Company)
        return (await session.execute(stmt)).scalars().all()
