from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers.states import LeadForm
from db.db import add_lead
from config import MANAGER_CHAT_ID
from loguru import logger
import re

from keyboards.keyboards import cancel_keyboard, new_lead_keyboard, remove_keyboard

router = Router()

# Вспомогательная функция для обработки "Отменить"
async def check_cancel(message: Message, state: FSMContext):
    if message.text == "❌ Отменить":
        await state.clear()
        await message.answer("Заполнение заявки отменено.", reply_markup=remove_keyboard)
        return True
    return False

# Старт формы — приветствие и запрос имени
@router.message(F.text == "/start")
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Здравствуйте! Пожалуйста, введите ваше имя:",
        reply_markup=cancel_keyboard
    )
    await state.set_state(LeadForm.waiting_for_name)
    logger.info(f"Пользователь {message.from_user.id} начал заполнение заявки.")

# Получение имени
@router.message(LeadForm.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    if await check_cancel(message, state):
        return
    await state.update_data(name=message.text)
    await message.answer(
        "Введите ваш номер телефона (например, +79991234567):",
        reply_markup=cancel_keyboard
    )
    await state.set_state(LeadForm.waiting_for_phone)

# Валидация телефона
@router.message(LeadForm.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext):
    if await check_cancel(message, state):
        return
    phone = message.text.strip()
    if not re.match(r"^\+?\d{10,15}$", phone):
        await message.answer("Пожалуйста, введите корректный номер телефона (например, +79991234567):")
        return
    await state.update_data(phone=phone)
    await message.answer(
        "Опишите ваш запрос:",
        reply_markup=cancel_keyboard
    )
    await state.set_state(LeadForm.waiting_for_request)

# Получение запроса и завершение формы
@router.message(LeadForm.waiting_for_request)
async def process_request(message: Message, state: FSMContext, bot):
    if await check_cancel(message, state):
        return
    data = await state.get_data()
    name = data["name"]
    phone = data["phone"]
    request_message = message.text

    # Сохраняем заявку в базу данных
    await add_lead(name, phone, request_message)
    logger.info(f"Заявка от {name} ({phone}) сохранена.")

    # Уведомляем менеджера
    notification = (
        f"Новая заявка!\n"
        f"Имя: {name}\n"
        f"Телефон: {phone}\n"
        f"Запрос: {request_message}\n"
    )
    await bot.send_message(chat_id=int(MANAGER_CHAT_ID), text=notification)
    logger.info(f"Заявка отправлена менеджеру: {MANAGER_CHAT_ID}")

    await message.answer(
        "Спасибо! Ваша заявка отправлена.",
        reply_markup=new_lead_keyboard
    )
    await state.clear()

# Обработка кнопки "Заполнить новую заявку"
@router.message(F.text == "📝 Заполнить новую заявку")
async def new_lead(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Пожалуйста, введите ваше имя:",
        reply_markup=cancel_keyboard
    )
    await state.set_state(LeadForm.waiting_for_name)
