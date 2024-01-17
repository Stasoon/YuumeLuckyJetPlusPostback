import random

from aiogram import quote_html

from src.create_bot import _


class Messages:
    #  Статья с фото: https://telegra.ph/Foto-dlya-yuume-tg-bota-12-12

    @staticmethod
    def ask_for_locale() -> str:
        return 'Выберите язык ⤵️\n' \
               'What is your language? ⤵'

    @staticmethod
    def get_welcome(user_name: str = 'незнакомец') -> str:
        return _(
            f"Добро пожаловать, <u>{quote_html(user_name)}</u>! \n\n"
            "⚙ Здесь вы можете получить <b>инструкцию по входу в VIP-канал</b>, "
            "где мы даём сигналы с помощью нашего бота. \n\n"
            "🔑 <b>С помощью VIP-канала вы сможете заработать на месячный тариф и получить самого БОТА.</b> \n\n"
            "🔊 Также обязательно подпишитесь на <a href='https://t.me/+WZCtVDD5A_5jOGY6'>наш канал</a>, "
            "где есть много полезной информации \n\n"
            "<b>И только после этого Вы сможете получать сигналы!</b>"
        )

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
            '❗ Нужно создать <b>НОВЫЙ аккаунт</b> по кнопке ниже, <b>введя промо «<code>JET360</code>»</b>, '
            'это необходимо для того, чтобы <b>софт мог идентифицировать вас</b>. \n\n'
            '📲 Если у вас нет лишнего номера для создания аккаунта, <b>можете использовать социальные сети.</b>'
        )

    @staticmethod
    def get_registration_not_passed() -> str:
        return _(
            '<b>РЕГИСТРАЦИЯ НЕ ПРОЙДЕНА</b> ❌ \n\n'
            '‼ <b>ОЧЕНЬ ВАЖНО</b>, если у вас уже есть аккаунт, вам нужно зарегистрировать '
            '<b>НОВУЮ учетную запись</b> по кнопке ниже, чтобы сигналы в VIP канале совпадали с вашими, '
            '<b>так как бот работает на другом сервере.</b> \n\n'
            '🤖 Чтобы бот смог проверить вашу регистрацию, <b>обязательно нужно ввести промокод'
            ' «<code>JET360</code>» при регистрации!</b>'
        )

    @staticmethod
    def get_registration_not_passed_photo() -> str:
        return 'https://telegra.ph/file/dfbec0ab7e19299c95718.png'

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

    # @staticmethod
    # def get_next_signal(onewin_id: int):
    #     coefficient = f'{random.uniform(1.30, 2.73):.2f}'
    #     return _('ID: {onewin_id} \n🚀 ВЫВОДИ НА: <b>{coefficient}</b>') \
    #         .format(onewin_id=onewin_id, coefficient=coefficient)
    #
    # @staticmethod
    # def ask_for_code_word() -> str:
    #     return _('🔐 Для использования бота, введите «кодовое слово» которое вам выдали:')
    #
    # @staticmethod
    # def get_code_word_incorrect():
    #     return _('❗<b>Вы ввели неправильное кодовое слово!</b> \nПопробуйте ещё раз:')
    #
    # @staticmethod
    # def ask_for_1win_id() -> str:
    #     return _('Замечательно! \nТеперь введите 🆔 от вашего аккаунта 1win: ')
    #
    # @staticmethod
    # def get_1win_id_incorrect_length() -> str:
    #     return _('❗<b>ID не может содержать букв и символов, только цифры!</b> \nПопробуйте ещё раз:')
    #
    # @staticmethod
    # def get_1win_id_have_forbidden_symbols() -> str:
    #     return _('❗<b>ID должно иметь длину в 8 цифр</b> \nПопробуйте снова:')
    #
    # @staticmethod
    # def get_before_game_start() -> str:
    #     return _("Перед тем как, начать ⤵️\n\n"
    #              "Минимальная сумма депозита в игре с ботом <b>500-1000₽</b> либо <b>5-15$</b> \n\n"
    #              "Если вдруг бот выдает не верные коэффициенты, скорее всего ваш аккаунт <b>не активирован</b>. \n"
    #              "Нужно сделать депозит еще раз, чтобы ваш аккаунт активировался❗")
    #
    # @staticmethod
    # def get_before_start_photo() -> str:
    #     return 'AgACAgIAAxkBAAEB_TtkzMl5s-HsM8JstC6FO4PRc4b6SAAC3cYxG5rOaErWm2hpoDD2pQEAAwIAA3kAAy8E'
