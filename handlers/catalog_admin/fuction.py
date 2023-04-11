from aiogram.fsm.context import FSMContext
from aiogram.types import InputMediaPhoto


async def get_value(self, key):
    data = await self.get_data()
    value = data[key]
    return value


async def get_media(photos=None, state=None):
    media = []
    if state:
        data = await state.get_data()
        photos = data['photos']
    for ph in photos:
        media.append(
            InputMediaPhoto(type='photo', media=ph)
        )
    return media


async def update_list(state, key, value):
    data = await state.get_data()
    ls = data[key]
    ls.append(value)
    return ls


