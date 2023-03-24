from aiogram.dispatcher.filters.state import StatesGroup, State


class AddProductStates(StatesGroup):
    getTittle = State()
    getPhoto = State()
    addOption = State()
    getCaption = State()
    getPrice = State()