from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    phoneNumber = State()
    fullName = State()
    course = State()
    confirm = State()
