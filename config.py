from dotenv import load_dotenv
import os

# Загружаем переменные из .env (если он есть)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MANAGER_CHAT_ID = os.getenv("MANAGER_CHAT_ID")
MANAGER_USER_ID = os.getenv("MANAGER_USER_ID")

# Настройки базы данных
DB_PATH = os.getenv("DB_PATH", "./leads.db")  # По умолчанию SQLite в корне проекта

# Если используешь PostgreSQL, раскомментируй и используй эти переменные
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
