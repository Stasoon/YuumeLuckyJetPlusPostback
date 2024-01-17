from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import CallbackData


class Keyboards:
    locale_callback_data = CallbackData('locale', 'language_code')

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
        subscribe_button = InlineKeyboardButton(text='🔊 ПОДПИСАТЬСЯ НА КАНАЛ 🔊', url=channel_url)
        free_access_button = InlineKeyboardButton(text='🔒 БЕСПЛАТНЫЙ ДОСТУП 🔒', callback_data='free_access')

        return InlineKeyboardMarkup(row_width=1).add(subscribe_button, free_access_button)

    @staticmethod
    def get_receive_signals() -> InlineKeyboardMarkup:
        receive_button = InlineKeyboardButton(text='🤖 ПРОУЧИТЬ СИГНАЛЫ 🤖', callback_data='receive_signals')
        return InlineKeyboardMarkup(row_width=1).add(receive_button)

    @staticmethod
    def get_registration() -> InlineKeyboardMarkup:
        registration_link = 'https://1wauah.xyz'
        registration_link_button = InlineKeyboardButton(text='📲 РЕГИСТРАЦИЯ', url=registration_link)
        check_registration = InlineKeyboardButton(text='🔎 ПРОВЕРИТЬ РЕГИСТРАЦИЮ', callback_data='check_registration')

        return InlineKeyboardMarkup(row_width=1).add(registration_link_button, check_registration)

    @staticmethod
    def get_check_deposit() -> InlineKeyboardMarkup:
        check_deposit = InlineKeyboardButton(text='✅ ПРОВЕРИТЬ ДЕПОЗИТ', callback_data='check_deposit')
        return InlineKeyboardMarkup(row_width=1).add(check_deposit)

    # @staticmethod
    # def get_first_signal_markup() -> InlineKeyboardMarkup:
    #     first_signal = InlineKeyboardButton(_('▶ ПОЛУЧИТЬ СИГНАЛ ▶'), callback_data='next_signal')
    #     return InlineKeyboardMarkup(row_width=2).add(first_signal)
    #
    # @staticmethod
    # def get_next_signal_markup() -> InlineKeyboardMarkup:
    #     next_signal = InlineKeyboardButton(_('СЛЕДУЮЩИЙ РАУНД ➡'), callback_data='next_signal')
    #     return InlineKeyboardMarkup(row_width=2).add(next_signal)

