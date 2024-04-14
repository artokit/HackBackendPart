import time
from fastapi import HTTPException
from jwt import InvalidTokenError
from starlette import status
from fastapi import Depends
from auth.models import User
from auth.roles import Roles
from auth.utils import encode_jwt, check_password, decode_jwt
from config import ACCESS_TOKEN_EXPIRE_DAYS
from auth.schemas import UserRegister, SuccessAuth, UserLogin
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
from auth import repo

http_bearer = HTTPBearer()
oauth_bearer = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def register( user: UserRegister):
    if await repo.exist_telegram_user(user.telegram_user):
        raise HTTPException(
            detail="Данный телеграм уже занят",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    if not user.telegram_user.startswith("@") and user.telegram_user.count("@") != 1:
        raise HTTPException(
            detail="Неверный телеграм",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    if not user.full_name.count(" ") != 3 and not user.full_name.isalpha():
        raise HTTPException(
            detail="Неверный формат ФИО",
            status_code=status.HTTP_400_BAD_REQUEST
        )

    if await repo.exist_email(user.email):
        raise HTTPException(
            detail='Почта уже занята',
            status_code=status.HTTP_400_BAD_REQUEST
        )

    user = await repo.add_user(user)
    payload = {
        "exp": time.time() + ACCESS_TOKEN_EXPIRE_DAYS * 60 * 60 * 24,
        "id": user.id,
        "role": user.role
    }
    return SuccessAuth(
        access_token=encode_jwt(payload),
        token_type="Bearer"
    )


async def login( user_login: UserLogin):
    res = await repo.get_user_by_email(user_login.email)
    exc = HTTPException(
        detail="Неверный логин/пароль",
        status_code=status.HTTP_401_UNAUTHORIZED
    )

    if not res:
        raise exc

    if not check_password(user_login.password, res.hashed_password.encode()):
        raise exc

    payload = {
        "exp": time.time() + ACCESS_TOKEN_EXPIRE_DAYS * 60 * 60 * 24,
        "id": res.id,
        "role": res.role
    }
    return SuccessAuth(
        access_token=encode_jwt(payload),
        token_type="Bearer"
    )


async def get_user(id: int):
    return await repo.get_user_by_id(id)


async def get_current_auth_user(
        token: str = Depends(oauth_bearer)
):
    return True
    try:
        payload = decode_jwt(token)
        user = await get_user(payload["id"])
        return user

    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error {e}"
        )


async def current_user_is_admin(user: User = Depends(get_current_auth_user)):
    if user.role != Roles.ADMIN.value:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Недостаточно прав")

    return user
