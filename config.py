from pydantic import BaseSettings
from telebot import TeleBot


class Settings(BaseSettings):
    PORT : int
    DB_NAME: str
    MONGODB_URI : str
    BEARER: str
    TOKEN : str

    class Config:
        env_file = '.env'

config = Settings()

print(config)

BOT = TeleBot(config.TOKEN)