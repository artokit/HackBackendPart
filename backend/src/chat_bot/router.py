from fastapi import APIRouter
from chat_bot import service
from chat_bot.schemas import History

router = APIRouter(prefix="/api/chat_bot", tags=["chat_bot"])


@router.get("/history", response_model_exclude_unset=True, response_model=History)
async def get_history():
    return service.get_history()
