from typing import Annotated
from fastapi import APIRouter, Form
from auth.schemas import UserRegister, UserLogin, SuccessAuth
from auth import service

router = APIRouter(prefix='/api/auth', tags=['Auth'])


@router.post("/register", response_model=SuccessAuth)
async def register(
        user_register: UserRegister,
):
    return await service.register(user_register)


@router.post("/login", response_model=SuccessAuth)
async def login(
        username: Annotated[str, Form()],
        password: Annotated[str, Form()]
):
    return await service.login(UserLogin(email=username, password=password))
