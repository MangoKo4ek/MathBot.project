import os
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv('DB')
BOT_TOKEN = os.getenv('BOT_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')
ADMIN_ID = os.getenv('ADMIN_ID')
