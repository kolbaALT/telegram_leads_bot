from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# Кнопка "Отменить"
cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❌ Отменить")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Клавиатура после отправки заявки
new_lead_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Заполнить новую заявку")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Клавиатура без кнопок (скрыть)
remove_keyboard = ReplyKeyboardRemove()
