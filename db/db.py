import aiosqlite
from datetime import datetime

DB_PATH = "leads.db"  # Путь к базе данных (можно заменить на config.DB_PATH)

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                request_message TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        await db.commit()

async def add_lead(name: str, phone: str, request_message: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO leads (name, phone, request_message, created_at)
            VALUES (?, ?, ?, ?)
        ''', (name, phone, request_message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        await db.commit()

async def get_all_leads():
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute('SELECT * FROM leads') as cursor:
            return await cursor.fetchall()
