from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"))

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
ACCESS_TOKEN_EXPIRE_DAYS = 7
CERTS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "certs")
