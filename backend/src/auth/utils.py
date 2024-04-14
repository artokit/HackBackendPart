import jwt
from auth.config import settings
import bcrypt


def encode_jwt(data: dict):
    encoded = jwt.encode(data, settings.auth_jwt.private_key, algorithm=settings.auth_jwt.algorithm)
    return encoded


def decode_jwt(token):
    return jwt.decode(token, settings.auth_jwt.public_key, algorithms=[settings.auth_jwt.algorithm])


def hash_password(password: str) -> bytes:
    hashed = password.encode()
    return bcrypt.hashpw(hashed, bcrypt.gensalt())


def check_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password)
