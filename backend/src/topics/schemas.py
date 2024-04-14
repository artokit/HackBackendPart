from pydantic import BaseModel


class SuccessAddCategory(BaseModel):
    id: int
    name: str


class AddTopic(BaseModel):
    category_id: int
    title: str
    content: str
    telegram_name: str


class SuccessAddTopic(BaseModel):
    id: int
    category: str
    title: str
    content: str
    telegram_name: str


class TopicResponse(BaseModel):
    id: int
    title: str
    content: str
    telegram_name: str


class AllCategoriesResponse(BaseModel):
    res: list[SuccessAddCategory]


class CategoryTopic(BaseModel):
    id: int
    category_name: str
    topics: list[TopicResponse]


class GetAllTopicsByCategory(BaseModel):
    res: list[CategoryTopic]
