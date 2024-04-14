from typing import Optional
from pydantic import BaseModel


class SendText(BaseModel):
    message: str


class Answer(BaseModel):
    id: str
    text: list[str]
    my: bool
    meta: Optional[dict] = None


class History(BaseModel):
    history: list[Answer]
