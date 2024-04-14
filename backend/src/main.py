from auth.router import router as auth_router
from topics.router import router as topics_router
from hubs.router import router as hubs_router
from maps.router import router as maps_router
from chat_bot.router import router as chat_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(topics_router)
app.include_router(hubs_router)
app.include_router(maps_router)
app.include_router(chat_router)
