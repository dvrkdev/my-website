import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration, default values."""

    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-fallback-key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///default.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
