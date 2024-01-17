from aiogram.dispatcher.filters import State, StatesGroup


class UserDataInputting(StatesGroup):
    wait_for_password = State()
    wait_for_id = State()
