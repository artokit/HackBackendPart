from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    telegram_user: str


class UserLogin(BaseModel):
    email: str
    password: str


class SuccessAuth(BaseModel):
    access_token: str
    token_type: str
