from aiogram.utils.markdown import quote_html

from src.create_bot import _


promo_code = 'JET360'


class Messages:
    #  Статья с фото: https://telegra.ph/Foto-dlya-yuume-tg-bota-12-12

    @staticmethod
    def ask_for_locale() -> str:
        return 'Выберите язык ⤵️\n' \
               'What is your language? ⤵'

    @staticmethod
    def get_welcome(user_name: str = 'незнакомец') -> str:
        return _(
            "Добро пожаловать, <u>{user_name}</u>! \n\n"
            "⚙ Здесь вы можете получить <b>инструкцию по входу в VIP-канал</b>, "
            "где мы даём сигналы с помощью нашего бота. \n\n"
            "🔑 <b>С помощью VIP-канала вы сможете заработать на месячный тариф и получить самого БОТА.</b> \n\n"
            "🔊 Также обязательно подпишитесь на <a href='{channel_url}'>наш канал</a>, "
            "где есть много полезной информации \n\n"
            "<b>И только после этого Вы сможете получать сигналы!</b>"
        ).format(user_name=quote_html(user_name), channel_url='https://t.me/+WZCtVDD5A_5jOGY6')

    @staticmethod
    def get_welcome_photo() -> str:
        return 'https://telegra.ph/file/7e6427992b877389a0bbf.png'

    @staticmethod
    def get_vip_examples() -> str:
        return _(
            '<b>Фрагмент нашей работы по сигналам из VIP☝</b> \n\n'
            '<b>В VIP группе:</b> \n'
            '✔ Сигналы от нашего уникального бота \n'
            '✔ Раздача бота активным участникам \n'
            '✔ Навигация по стратегиям + видео инструкции \n'
            '✔ Ежемесячные раздачи денег'
        )

    @staticmethod
    def get_vip_examples_video() -> str:
        return 'https://telegra.ph/file/18e788d46b5c8ce8c81df.mp4'

    @staticmethod
    def get_registration_tutorial() -> str:
        return _(
            '⤵ <b>Регистрация аккаунта </b> \n\n'
            '❗ Нужно создать <b>НОВЫЙ аккаунт</b> по кнопке ниже, <b>введя промо «<code>{promo}</code>»</b>, '
            'это необходимо для того, чтобы <b>софт мог идентифицировать вас</b>. \n\n'
            '📲 Если у вас нет лишнего номера для создания аккаунта, <b>можете использовать социальные сети.</b>'
        ).format(promo=promo_code)

    @staticmethod
    def get_registration_tutorial_photo() -> str:
        return 'https://telegra.ph/file/b28d7cd35a6a5578fa8f6.png'

    @staticmethod
    def get_registration_not_passed() -> str:
        return _(
            '<b>РЕГИСТРАЦИЯ НЕ ПРОЙДЕНА</b> ❌ \n\n'
            '‼ <b>ОЧЕНЬ ВАЖНО</b>, если у вас уже есть аккаунт, вам нужно зарегистрировать '
            '<b>НОВУЮ учетную запись</b> по кнопке ниже, чтобы сигналы в VIP канале совпадали с вашими, '
            '<b>так как бот работает на другом сервере.</b> \n\n'
            '🤖 Чтобы бот смог проверить вашу регистрацию, <b>обязательно нужно ввести промокод'
            ' «<code>{promo}</code>» при регистрации!</b>'
        ).format(promo=promo_code)

    @staticmethod
    def get_registration_not_passed_photo() -> str:
        return _('registration_not_passed_photo')  # 'https://telegra.ph/file/dfbec0ab7e19299c95718.png'

    @staticmethod
    def get_registration_passed() -> str:
        return _(
            '<b>РЕГИСТРАЦИЯ ПРОЙДЕНА</b> ✅ \n\n'
            'Теперь нужно активировать аккаунт. Активация происходит <b>«пополнением баланса»</b> от 10$. \n\n'
            'После активации автоматически выдается доступ к VIP каналу 🔑'
        )

    @staticmethod
    def get_registration_passed_photo() -> str:
        return 'https://telegra.ph/file/5e4f9ef3fc867b868d50d.png'

    @staticmethod
    def get_deposit_not_found() -> str:
        return _('❗ Ваш депозит не найден')

    @staticmethod
    def get_welcome_to_vip() -> str:
        vip_url = 'https://t.me/+8IwwNU0oMXAxZGJi'
        return _(
            '<b>Добро пожаловать в VIP ✅</b> \n\n'
            '<b>Друг напоминаю, в VIP-канале, ты получишь самые бомбовые сигналы на рынке</b> 📈 \n\n'
            '❗<b>ВАЖНО</b>, на старом аккаунте нельзя играть, иначе могут заблокировать счёт, играешь только на том, '
            'который создал, так же рекомендую не создавать новые аккаунты, <b>чтобы избежать '
            'блокировок за мультиаккаунты.</b> \n\n'
            'Об этом многие не говорят, но всё прописано в политике конфиденциальности платформы <b>доступ ниже, '
            'удачи бро, топи</b> 💰 \n\n'
            '🔑 {vip_url}'
        ).format(vip_url=vip_url)
