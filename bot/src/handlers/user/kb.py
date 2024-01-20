from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from src.create_bot import _


one_win_registration_link = 'https://1wowei.xyz/casino/list?open=register#h1bi'


class Keyboards:
    locale_callback_data = CallbackData('locale', 'language_code')
    deposit_check_callback = CallbackData('check_dep', 'one_win_id')

    @staticmethod
    def get_choose_locale() -> InlineKeyboardMarkup:
        ru_button = InlineKeyboardButton(
            text='Русский 🇷🇺', callback_data=Keyboards.locale_callback_data.new(language_code='ru'))
        eng_button = InlineKeyboardButton(
            text='English 🇬🇧', callback_data=Keyboards.locale_callback_data.new(language_code='en'))

        return InlineKeyboardMarkup(row_width=1).add(ru_button, eng_button)

    @staticmethod
    def get_welcome_menu() -> InlineKeyboardMarkup:
        channel_url = 'https://t.me/+WZCtVDD5A_5jOGY6'
        subscribe_button = InlineKeyboardButton(text=_('🔊 ПОДПИСАТЬСЯ НА КАНАЛ 🔊'), url=channel_url)
        free_access_button = InlineKeyboardButton(text=_('🔒 БЕСПЛАТНЫЙ ДОСТУП 🔒'), callback_data='free_access')

        return InlineKeyboardMarkup(row_width=1).add(subscribe_button, free_access_button)

    @staticmethod
    def get_receive_signals() -> InlineKeyboardMarkup:
        receive_button = InlineKeyboardButton(text=_('🤖 ПОЛУЧИТЬ СИГНАЛЫ 🤖'), callback_data='receive_signals')
        return InlineKeyboardMarkup(row_width=1).add(receive_button)

    @staticmethod
    def get_create_account() -> InlineKeyboardMarkup:
        registration_link_button = InlineKeyboardButton(text=_('🔑 СОЗДАТЬ АККАУНТ'), url=one_win_registration_link)
        check_registration = InlineKeyboardButton(text=_('🔎 ПРОВЕРИТЬ РЕГИСТРАЦИЮ'), callback_data='check_registration')
        return InlineKeyboardMarkup(row_width=1).add(registration_link_button, check_registration)

    @staticmethod
    def get_registration() -> InlineKeyboardMarkup:
        registration_link_button = InlineKeyboardButton(text=_('📲 РЕГИСТРАЦИЯ'), url=one_win_registration_link)
        check_registration = InlineKeyboardButton(text=_('🔎 ПРОВЕРИТЬ РЕГИСТРАЦИЮ'), callback_data='check_registration')
        return InlineKeyboardMarkup(row_width=1).add(registration_link_button, check_registration)

    @classmethod
    def get_check_deposit(cls, one_win_id: int) -> InlineKeyboardMarkup:
        check_deposit = InlineKeyboardButton(
            text=_('🔐 ПРОВЕРИТЬ ДЕПОЗИТ'),
            callback_data=cls.deposit_check_callback.new(one_win_id=one_win_id)
        )
        return InlineKeyboardMarkup(row_width=1).add(check_deposit)
