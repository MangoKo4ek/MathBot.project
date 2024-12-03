import aiosqlite


async def initialize_database():
    # Подключаемся к базе данных (если база данных не существует, она будет создана)
    async with aiosqlite.connect("bot.db") as db:
        await db.execute("""
                    CREATE TABLE IF NOT EXISTS channels (
                        telegram_id INTEGER PRIMARY KEY,
                        username TEXT,
                        first_name TEXT,
                        bot_open BOOLEAN DEFAULT FALSE
                    )
                """)
        # Сохраняем изменения
        await db.commit()