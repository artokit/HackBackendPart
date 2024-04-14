import os
from pydantic import BaseModel
from pydantic.v1 import BaseSettings
from config import CERTS_PATH


class AuthJWT(BaseModel):
    private_key: str = open(os.path.join(CERTS_PATH, 'private.pem'), 'r').read()
    public_key: str = open(os.path.join(CERTS_PATH, 'public.pem'), 'r').read()
    algorithm: str = "RS256"


class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
