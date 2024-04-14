from sqlalchemy import insert, select
from topics.models import TopicCategory, Topic
from db.db import async_session_maker
from topics.schemas import AddTopic, GetAllTopicsByCategory, TopicResponse


async def add_topic_category(name: str) -> TopicCategory:
    async with async_session_maker() as session:
        stmt = insert(TopicCategory).values(name=name).returning(TopicCategory)
        res = await session.execute(stmt)
        await session.commit()
        return (res.fetchone())[0]


async def add_topic(topic: AddTopic) -> Topic:
    async with async_session_maker() as session:
        stmt = insert(Topic).values(
            category_id=topic.category_id,
            title=topic.title,
            content=topic.content,
            telegram_name=topic.telegram_name
        ).returning(Topic)
        res = await session.execute(stmt)
        await session.commit()
        return (res.fetchone())[0]


async def get_topic_category_by_id(id) -> TopicCategory:
    async with async_session_maker() as session:
        stmt = select(TopicCategory).where(TopicCategory.id == id)
        res = (await session.execute(stmt)).fetchone()

        if res:
            return res[0]


async def get_all_topic_categories() -> list[TopicCategory]:
    async with async_session_maker() as session:
        stmt = select(TopicCategory)
        return (await session.scalars(stmt)).all()


async def get_topic_by_category_id(category_id: int) -> list[TopicResponse]:
    async with async_session_maker() as session:
        stmt = select(Topic).where(Topic.category_id == category_id)
        res = (await session.execute(stmt)).scalars()
        return [TopicResponse(id=i.id, title=i.title, content=i.content, telegram_name=i.telegram_name) for i in res]
