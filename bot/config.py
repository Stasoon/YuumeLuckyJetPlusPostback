import os
from typing import Final
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


CHANNEL_ID = -1001701565036
CHANNEL_URL = 'https://t.me/+WZCtVDD5A_5jOGY6'


class Config:
    TOKEN: Final = os.getenv('BOT_TOKEN', 'Впишите токен в .env!')
    ADMIN_IDS: Final = tuple(int(i) for i in str(os.getenv('BOT_ADMIN_IDS')).split(','))

    LOCALES_DIR = 'locales'
    I18N_DOMAIN = 'messages'