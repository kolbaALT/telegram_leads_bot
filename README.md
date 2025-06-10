# Telegram Leads Bot

Бот для сбора клиентских заявок через Telegram без использования сайта.  
Заявки сохраняются в базу данных и отправляются менеджеру в приватный чат.

---

## Возможности

- Пошаговый сбор данных пользователя (имя, телефон с валидацией, запрос)
- Сохранение заявок в базу данных (SQLite)
- Уведомление менеджера о новых заявках
- Просмотр всех заявок командой `/leads` (только для менеджера)
- FSM (Finite State Machine) для последовательного диалога
- Логирование действий и ошибок
- Удобные Telegram-кнопки ("Отменить", "Заполнить новую заявку")

---

## Требования

- Python 3.10+
- [aiogram](https://docs.aiogram.dev/) 3.x
- SQLite (по умолчанию, можно подключить PostgreSQL)
- Telegram аккаунт

---


---

## Быстрый старт

### 1. Клонируй репозиторий

git clone https://github.com/your_username/telegram_leads_bot.git
cd telegram_leads_bot


### 2. Создай и активируй виртуальное окружение

python -m venv venv

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate


### 3. Установи зависимости

pip install -r requirements.txt



### 4. Настрой файл окружения

- Скопируй `.env.example` в `.env`:
cp .env.example .env

- Заполни значения:
- `BOT_TOKEN` — токен бота из BotFather
- `MANAGER_CHAT_ID` — chat_id менеджера (кому отправлять заявки)
- `MANAGER_USER_ID` — user_id менеджера (кто может использовать /leads)

### 5. Запусти бота

python main.py


---

## Как получить токен и chat_id

1. Создай бота через [@BotFather](https://t.me/BotFather) и получи токен.
2. Узнай свой user_id и chat_id через бота [@userinfobot](https://t.me/userinfobot) или [@getmyid_bot](https://t.me/getmyid_bot).

---

## Команды бота

- `/start` — начать заполнение заявки
- `/leads` — просмотр всех заявок (только для менеджера)

---

## Безопасность

- **Никогда не публикуй файл `.env`** — используй только `.env.example` для примера.
- Не выкладывай свои токены и пароли в публичный доступ.

---

## Лицензия

MIT

---

## Обратная связь

Если возникли вопросы или предложения — создайте issue или pull request в этом репозитории.


