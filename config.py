from dotenv import load_dotenv

import os

load_dotenv()

class Settings:
    EXTERNAL_API_URL = os.environ["EXTERNAL_API_URL"]
    DATABASE_URL = os.environ["DATABASE_URL"]
    PORT = os.getenv("PORT", 8080)
    ENV = os.environ.get("ENV", "production")

settings = Settings()