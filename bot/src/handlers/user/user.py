from aiogram import Dispatcher

from aiogram.types import CallbackQuery, Message, InputMediaVideo, InputMediaPhoto
from peewee import fn

from src.database import users
from src.utils import send_typing_action, throttle
from .messages import Messages
from .kb import Keyboards
from src.create_bot import i18n

from src.database.models import OneWinRegistration, OneWinDeposit


@throttle()
async def __handle_start_command(message: Message) -> None:
    await send_typing_action(message)
    users.create_or_update_user(
        telegram_id=message.from_id,
        name=message.from_user.username or message.from_user.full_name,
        reflink=message.get_full_command()[1]
    )

    await message.answer(text=Messages.ask_for_locale(), reply_markup=Keyboards.get_choose_locale())


async def __handle_locale_callback(callback: CallbackQuery, callback_data: Keyboards.locale_callback_data):
    await send_typing_action(callback.message)
    await callback.message.delete()

    # Устанавливаем выбранный язык
    language_code = callback_data.get('language_code')
    users.set_locale(callback.from_user.id, language_code)
    i18n.change_locale_context(lang_code=language_code)

    await callback.message.answer_photo(
        photo=Messages.get_welcome_photo(),
        caption=Messages.get_welcome(callback.from_user.first_name),
        reply_markup=Keyboards.get_welcome_menu(),
    )


async def __handle_free_access_callback(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaVideo(media=Messages.get_vip_examples_video(), caption=Messages.get_vip_examples()),
        reply_markup=Keyboards.get_receive_signals(),
    )


async def __handle_receive_signals_callback(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer_photo(
        photo=Messages.get_registration_tutorial_photo(),
        caption=Messages.get_registration_tutorial(),
        reply_markup=Keyboards.get_registration(user_telegram_id=callback.from_user.id),
    )


async def __handle_check_registration_callback(callback: CallbackQuery):
    user_one_win_registration = OneWinRegistration.get_or_none(OneWinRegistration.sub_id == callback.from_user.id)

    if user_one_win_registration:
        text = Messages.get_registration_passed()
        photo = Messages.get_registration_passed_photo()
        markup = Keyboards.get_check_deposit()

        await callback.message.edit_media(media=InputMediaPhoto(media=photo, caption=text), reply_markup=markup)
    else:
        await callback.message.edit_reply_markup(reply_markup=None)
        text = Messages.get_registration_not_passed()
        photo = Messages.get_registration_not_passed_photo()
        markup = Keyboards.get_registration(user_telegram_id=callback.from_user.id)

        await callback.message.answer_photo(photo=photo, caption=text, reply_markup=markup)


async def __handle_check_deposit_callback(callback: CallbackQuery):
    user_deposits_sum = (
        OneWinDeposit
        .select(fn.SUM(OneWinDeposit.amount))
        .where(OneWinDeposit.sub_id == callback.from_user.id)
        .scalar()
    )

    if user_deposits_sum and user_deposits_sum < 10.0:
        await callback.answer(text=Messages.get_deposit_not_found(), show_alert=True)
    else:
        await callback.message.delete()
        await callback.message.answer(text=Messages.get_welcome_to_vip())


# endregion


def register_user_handlers(dp: Dispatcher) -> None:
    # обработка команды /start
    dp.register_message_handler(__handle_start_command, commands=['start'])

    # выбор языка
    dp.register_callback_query_handler(__handle_locale_callback, Keyboards.locale_callback_data.filter())

    # информация
    dp.register_callback_query_handler(__handle_free_access_callback, text='free_access')
    dp.register_callback_query_handler(__handle_receive_signals_callback, text='receive_signals')

    # регистрация
    dp.register_callback_query_handler(__handle_check_registration_callback, text='check_registration')
    dp.register_callback_query_handler(__handle_check_deposit_callback, text='check_deposit')
