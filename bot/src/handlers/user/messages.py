from aiogram.utils.markdown import quote_html

from config import CHANNEL_URL
from src.create_bot import _


promo_code = 'BOT360'


class Messages:
    #  Статья с фото: https://telegra.ph/Foto-dlya-yuume-tg-bota-12-12

    @staticmethod
    def get_start_sticker() -> str:
        return 'CAACAgIAAxkBAAECMkxlvkjaOTJzcxeULoLVUUqoFCCaJgACTCgAAg95WUuuGnhFtULX4TQE'

    @staticmethod
    def ask_for_locale() -> str:
        return (
            'Выберите язык ⤵️\n' 
            'What is your language? ⤵'
        )

    @staticmethod
    def get_welcome(user_name: str = 'незнакомец') -> str:
        return _(
            "Добро пожаловать, <u>{user_name}</u>! \n\n"
            "⚙ Здесь вы можете получить <b>бесплатный доступ к боту</b> который дает сигналы в игре <b>Lucky Jet</b> \n\n"
            "🔊 Также обязательно подпишитесь на <a href='{channel_url}'>наш канал</a>, где есть много полезной информации\n\n"
            "<b>И только после этого вы сможете получать сигналы ✅</b>"
        ).format(user_name=quote_html(user_name), channel_url=CHANNEL_URL)

    @staticmethod
    def get_welcome_photo() -> str:
        return 'https://telegra.ph/file/7e6427992b877389a0bbf.png'

    @staticmethod
    def get_subscription_needed() -> str:
        return _("Сначала подпишитесь на канал❗")

    @staticmethod
    def get_vip_examples() -> str:
        return _(
            "<b>Фрагмент работы БОТА ☝</b> \n\n"
            "<b><i>Что ты получишь? :</i></b> \n"
            "✔ Доход от 150$/день (переводи в свою валюту) \n"
            "✔ Удобные и стабильные сигналы \n"
            "✔ Поддержка и помощь по боту 24/7 \n"
        )

    @staticmethod
    def get_vip_examples_video() -> str:
        return 'https://telegra.ph/file/7303ec2c340c6a286d9ee.mp4'

    @staticmethod
    def get_registration_tutorial() -> str:
        return _(
            '⤵ <b>Регистрация аккаунта </b> \n\n'
            '❗ Нужно создать <b>НОВЫЙ аккаунт</b> по кнопке ниже, <b>введя промо «<code>{promo}</code>», '
            'чтобы БОТ мог идентифицировать вас.</b> \n\n'
            '📲 Если у вас нет лишнего номера для создания аккаунта, <b>можно использовать социальные сети.</b>'
        ).format(promo=promo_code)

    @staticmethod
    def get_registration_tutorial_photo() -> str:
        return 'https://telegra.ph/file/f03af5af4737ea56e3619.png'

    @staticmethod
    def get_ask_for_one_win_id() -> str:
        return _(
            '<b>Инструкция как найти свой ID на скриншоте выше ⬆</b> \n\n'
            '🔑 Отправьте сюда ID своего профиля для проверки:'
        )

    @staticmethod
    def get_ask_for_one_win_id_photo() -> str:
        return 'https://telegra.ph/file/7fb53587947eec232cb8d.png'

    @staticmethod
    def get_registration_not_passed() -> str:
        return _(
            '⚠ Упс! Я не вижу этот ID в базе \n\n'
            '❗Возможно, вы зарегистрировались не по ссылке. Либо ввели ID от старого аккаунта. \n\n'
            '🤖 <b>Обязательно вводи промокод «<code>{promo}</code>» при регистрации!</b> \n\n'
            'Это нужно для того, <b>чтобы бот смог вас идентифицировать</b> ✅'
        ).format(promo=promo_code)

    @staticmethod
    def get_id_should_be_digit_error_retry() -> str:
        return _('<b>ID должен состоять только из чисел!</b> \n\nПопробуйте ещё раз:')

    @staticmethod
    def get_registration_passed() -> str:
        return _(
            '<b>РЕГИСТРАЦИЯ ПРОЙДЕНА</b> ✅ \n\n'
            'Теперь нужно активировать аккаунт, <b>чтобы бот мог начать выдавать сигналы.</b> '
            'Активация происходит «<b>пополнением баланса</b>» от 10$. \n\n'
            '<b>После активации автоматически выдается доступ к БОТУ 🤖</b>'
        )

    @staticmethod
    def get_registration_passed_photo() -> str:
        return 'https://telegra.ph/file/5e4f9ef3fc867b868d50d.png'

    @staticmethod
    def get_deposit_not_found() -> str:
        return _('❗Ваш депозит не найден')

    @staticmethod
    def get_deposit_too_low() -> str:
        return _('❗Ваш депозит найден, но чтобы получить доступ в VIP, необходимо пополнение на сумму от 10$!')

    @staticmethod
    def get_welcome_to_vip() -> str:
        vip_url = 'https://t.me/+8IwwNU0oMXAxZGJi'
        return _(
            'Бесплатная версия БОТА находится на технических работах из-за обновления, <b>после окончания работ '
            'ты получишь доступ к боту</b> 🤖 \n\n'
            'В связи с этим, что бы не доставлять неудобств на момент пока ведутся тех работы, ты можешь '
            'воспользоваться нашим <b>приватным каналом</b> где выдаются сигналы из ПЛАТНОГО бота 📈 \n\n'
            '<b>Ссылка на приватный канал:</b> \n'
            '🔑 {vip_url} \n\n'
            '❗<b>ВАЖНО</b>, на старом аккаунте не стоит играть, иначе сигналы из нашего бота могут не совпадать, дабы '
            'избежать таких проблем, <b>рекомендую не менять игровой аккаунт.</b>'
        ).format(vip_url=vip_url)
