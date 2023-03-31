from aiogram.fsm.state import StatesGroup, State


class AddItemStates(StatesGroup):
    getTittle = State()
    getPhoto = State()
    getSubsequentPhoto = State()

    getTittleOptional = State()
    getPhotoOptional = State()
    getCaptionOptional = State()
    getPriceOptional = State()
