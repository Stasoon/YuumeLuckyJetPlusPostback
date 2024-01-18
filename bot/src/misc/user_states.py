from aiogram.dispatcher.filters.state import StatesGroup, State


class UserDataInputting(StatesGroup):
    wait_for_password = State()
    wait_for_id = State()
