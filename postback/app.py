from flask import Flask, request

from database import create_tables_if_not_exist, save_registration, save_deposit
from telegram import send_message
from config import TG_ADMIN_IDS, PORT
from logger import logger


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "I'm alive!"


@app.route("/reg", methods=['GET'])
def registration():
    one_win_id = request.args.get('user_id')

    save_registration(one_win_id=one_win_id)

    text = f"Регистрация: {one_win_id}"
    logger.info(text)
    for admin_id in TG_ADMIN_IDS:
        send_message(chat_id=admin_id, text=text)

    return 'OK: 200'


@app.route('/dep')
def deposit():
    one_win_id = request.args.get('user_id')
    amount = request.args.get('amount')

    save_deposit(one_win_id=one_win_id, amount=amount)

    text = f'{one_win_id} : депозит : {amount}'
    logger.info(text)
    for admin_id in TG_ADMIN_IDS:
        send_message(chat_id=admin_id, text=text)

    return 'OK: 200'


@app.route('/firstdep')
def first_deposit():
    one_win_id = request.args.get('user_id')
    amount = request.args.get('amount')

    save_deposit(one_win_id=one_win_id, amount=amount)

    text = f'{one_win_id} : первый депозит : {amount}'
    logger.info(text)
    for admin_id in TG_ADMIN_IDS:
        send_message(chat_id=admin_id, text=text)

    return 'OK: 200'


def run_app():
    logger.info('Приложение запущено')
    port = PORT
    app.run(host="0.0.0.0", port=port)


if __name__ == '__main__':
    create_tables_if_not_exist()
    run_app()
