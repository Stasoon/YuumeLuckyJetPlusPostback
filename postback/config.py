import os
from typing import Final
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN: Final[str] = os.getenv('BOT_TOKEN')
TG_ADMIN_IDS: Final[list[int]] = [int(adm_id) for adm_id in os.getenv('TG_ADMIN_IDS').split(',')]
DB_PATH: str = os.getenv('DB_PATH')
PORT: int = os.getenv('PORT', default=5000)
