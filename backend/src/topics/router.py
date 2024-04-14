from fastapi import APIRouter, Depends
from auth.service import current_user_is_admin, get_current_auth_user
from topics.schemas import SuccessAddCategory, AddTopic, SuccessAddTopic, GetAllTopicsByCategory, AllCategoriesResponse
from topics import service


router = APIRouter(prefix="/api/topics", tags=['Topics'])


@router.post("/add_category", response_model=SuccessAddCategory)
async def add_category(category_name: str):
    return await service.add_topic_category(category_name)


@router.post("/", response_model=SuccessAddTopic)
async def add_topic(topic: AddTopic):
    return await service.add_topic(topic)


@router.get("/", response_model=GetAllTopicsByCategory)
async def get_topics():
    return await service.get_all_topics_by_categories()


@router.get("/get_categories", response_model=AllCategoriesResponse)
async def get_categories():
    return await service.get_categories()
