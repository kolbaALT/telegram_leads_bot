from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❌ Отменить")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

new_lead_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Заполнить новую заявку")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

remove_keyboard = ReplyKeyboardRemove()
