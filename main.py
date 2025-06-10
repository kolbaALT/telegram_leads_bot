import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger

from config import BOT_TOKEN
from db.db import init_db

from handlers.user_form import router as user_form_router
from handlers.leads import router as leads_router

logger.add("bot.log", rotation="1 week", retention="1 month", encoding="utf-8")

async def main():
    logger.info("Запуск бота")
    await init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(user_form_router)
    dp.include_router(leads_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception(f"Ошибка при запуске бота: {e}")
