from typing import Optional
from topics import repo
from topics.models import TopicCategory
from topics.schemas import AddTopic, SuccessAddTopic, GetAllTopicsByCategory, CategoryTopic, AllCategoriesResponse, \
    SuccessAddCategory


async def add_topic_category(name: str) -> Optional[TopicCategory]:
    return await repo.add_topic_category(name)


async def add_topic(topic: AddTopic) -> SuccessAddTopic:
    res = await repo.add_topic(topic)
    return SuccessAddTopic(
        id=res.id,
        category=(await repo.get_topic_category_by_id(res.category_id)).name,
        title=res.title,
        content=res.content,
        telegram_name=res.telegram_name
    )


async def get_all_topics_by_categories() -> GetAllTopicsByCategory:
    categories = await repo.get_all_topic_categories()
    return GetAllTopicsByCategory(
        res=[CategoryTopic(
            id=i.id,
            category_name=i.name,
            topics=await repo.get_topic_by_category_id(i.id)
        ) for i in categories]
    )


async def get_categories() -> AllCategoriesResponse:
    return AllCategoriesResponse(
        res=[SuccessAddCategory(id=i.id, name=i.name) for i in await repo.get_all_topic_categories()]
    )
