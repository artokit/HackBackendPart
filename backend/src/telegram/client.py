from pyrogram import Client
from backend.src.config import API_HASH, API_ID

app = Client("anon", api_id=API_ID, api_hash=API_HASH)

app.start()


async def create_channel(channel_name: str):
    return await app.create_channel(channel_name)


async def get_count_user_in_channel(channel_id: int) -> int:
    return await app.get_chat_members_count(channel_id)

