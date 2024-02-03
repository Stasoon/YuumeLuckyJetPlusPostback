from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

from aiogram.types import CallbackQuery, Message
from peewee import fn

from src.database import users
from src.utils import send_typing_action
from .messages import Messages
from .kb import Keyboards
from src.create_bot import i18n

from src.database.models import OneWinRegistration, OneWinDeposit
from ...misc import UserRegistrationStates


async def __handle_start_command(message: Message, state: FSMContext) -> None:
    await state.finish()
    await send_typing_action(message)

    users.create_or_update_user(
        telegram_id=message.from_id,
        name=message.from_user.username or message.from_user.full_name,
        reflink=message.get_full_command()[1]
    )

    await message.answer_sticker(sticker=Messages.get_welcome_sticker())
    await message.answer(text=Messages.ask_for_locale(), reply_markup=Keyboards.get_choose_locale())


async def __handle_locale_callback(callback: CallbackQuery, callback_data: Keyboards.locale_callback_data):
    await callback.answer()
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
    await callback.answer()
    await callback.message.answer_video(
        video=Messages.get_vip_examples_video(),
        caption=Messages.get_vip_examples(),
        reply_markup=Keyboards.get_receive_signals(),
    )


async def __handle_receive_signals_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(
        photo=Messages.get_registration_tutorial_photo(),
        caption=Messages.get_registration_tutorial(),
        reply_markup=Keyboards.get_create_account(),
    )


async def __handle_check_registration_callback(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer_photo(
        photo=Messages.get_ask_for_one_win_id_photo(),
        caption=Messages.get_ask_for_one_win_id(),
        reply_markup=None
    )
    await state.set_state(UserRegistrationStates.enter_one_win_id.state)


async def __handle_one_win_id_message(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(text=Messages.get_id_should_be_digit_error_retry())
        return

    await state.finish()
    one_win_id = int(message.text)
    one_win_registration = OneWinRegistration.get_or_none(OneWinRegistration.one_win_id == one_win_id)

    if not one_win_registration:
        text = Messages.get_registration_not_passed()
        markup = Keyboards.get_registration()
        await message.answer(text=text, reply_markup=markup)
    else:
        text = Messages.get_registration_passed()
        photo = Messages.get_registration_passed_photo()
        markup = Keyboards.get_check_deposit(one_win_id=one_win_id)
        users.set_user_1win_id(telegram_id=message.from_user.id, onewin_id=one_win_id)
        await message.answer_photo(photo=photo, caption=text, reply_markup=markup)


async def __handle_check_deposit_callback(callback: CallbackQuery, callback_data: Keyboards.deposit_check_callback):
    user_deposits_sum = (
        OneWinDeposit
        .select(fn.SUM(OneWinDeposit.amount))
        .where(OneWinDeposit.one_win_id == callback_data.get('one_win_id'))
        .scalar()
    )

    if not user_deposits_sum:
        user_deposits_sum = 0.0

    min_rub_deposit_amount = 500.0

    if user_deposits_sum == 0:
        await callback.answer(text=Messages.get_deposit_not_found(), show_alert=True)
    elif user_deposits_sum < min_rub_deposit_amount:
        await callback.answer(text=Messages.get_deposit_too_low(), show_alert=True)
    else:
        await callback.message.delete()
        await callback.message.answer(text=Messages.get_welcome_to_vip())


# endregion


def register_user_handlers(dp: Dispatcher) -> None:
    # обработка команды /start
    dp.register_message_handler(__handle_start_command, commands=['start'], state='*')

    # выбор языка
    dp.register_callback_query_handler(__handle_locale_callback, Keyboards.locale_callback_data.filter())

    # информация
    dp.register_callback_query_handler(__handle_free_access_callback, text='free_access')
    dp.register_callback_query_handler(__handle_receive_signals_callback, text='receive_signals')

    # регистрация
    dp.register_callback_query_handler(__handle_check_registration_callback, text='check_registration')
    dp.register_message_handler(__handle_one_win_id_message, state=UserRegistrationStates.enter_one_win_id)
    dp.register_callback_query_handler(__handle_check_deposit_callback, Keyboards.deposit_check_callback.filter())
