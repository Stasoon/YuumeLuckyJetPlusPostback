import requests
from urllib.parse import urlencode
from loguru import logger

from config import BOT_TOKEN


API_URL = 'https://api.telegram.org/bot{token}/{method}?{params}'


def __get_params_string(params: dict) -> str:
    return urlencode(params)


def __post(method: str, params: dict) -> bool:
    url = API_URL.format(token=BOT_TOKEN, method=method, params=__get_params_string(params))
    response = requests.post(url=url)

    if response.status_code != 200:
        logger.error(f"Ошибка при отправке сообщения: {response.status_code}, {response.text}")
        return False
    return True


def send_message(chat_id: int, text: str):
    __post(
        method='sendMessage',
        params={'chat_id': chat_id, 'text': text}
    )
