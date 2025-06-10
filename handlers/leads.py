from aiogram import Router, F
from aiogram.types import Message
from db.db import get_all_leads
from config import MANAGER_USER_ID
from loguru import logger

router = Router()

@router.message(F.text == "/leads")
async def cmd_leads(message: Message):
    # Проверяем, что пользователь — менеджер
    if str(message.from_user.id) != str(MANAGER_USER_ID):
        await message.answer("У вас нет доступа к этой команде.")
        logger.warning(f"Пользователь {message.from_user.id} попытался получить доступ к /leads")
        return

    leads = await get_all_leads()
    if not leads:
        await message.answer("Заявок пока нет.")
        return

    response = "Список заявок:\n"
    for lead in leads:
        # lead: (id, name, phone, request_message, created_at)
        response += (
            f"\nID: {lead[0]}\n"
            f"Имя: {lead[1]}\n"
            f"Телефон: {lead[2]}\n"
            f"Запрос: {lead[3]}\n"
            f"Дата: {lead[4]}\n"
            + "-"*20 + "\n"
        )

    await message.answer(response)
    logger.info(f"Менеджер {message.from_user.id} просмотрел заявки.")
