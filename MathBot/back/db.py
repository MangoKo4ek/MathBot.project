import asyncio
import aiosqlite

from MathBot.config import DB_PATH


async def init_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    async with aiosqlite.connect(DB_PATH) as db:
        # Create a table
        await db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,      -- SQLite uses INTEGER for BIGINT
        points INTEGER,              -- Integer column for points
        first_name TEXT               -- Text column for strings
    )
""")
        await db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                points INTEGER,              
                text TEXT               
            )
        """)
        await db.commit()  # Commit the transaction

        # async with db.execute("SELECT id, message FROM greetings") as cursor:
        #     async for row in cursor:
        #         print(f"ID: {row[0]}, Message: {row[1]}")  # Print the result


asyncio.run(init_db())


async def create_user(user_id, first_name):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT INTO users (id, points, first_name) VALUES (?, ?, ?)", (user_id, 0, first_name))
        await db.commit()


async def user_exists(user_id: int) -> bool:
    """
    Проверяет, существует ли пользователь с заданным user_id в базе данных.

    :param user_id: ID пользователя для проверки.
    :return: True, если пользователь существует, иначе False.
    """
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT 1 FROM users WHERE id = ? LIMIT 1;", (user_id,)) as cursor:
            result = await cursor.fetchone()
            return result


async def task_base(text):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("Insert INTO tasks (points, text) VALUES (?, ?)", (3, text))
        await db.commit()
