from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


class IsDescriptionMessage(BaseFilter):
    async def __call__(self, msg: Message, state: FSMContext):
        data = await state.get_data()
        try:
            description_message = data['description_message_temp']
        except KeyError:
            return False

        if msg.message_id == description_message.message_id:
            return {'data': data}
        return False
