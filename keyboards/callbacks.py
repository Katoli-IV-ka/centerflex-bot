from aiogram.filters.callback_data import CallbackData


class SaveProductCall(CallbackData, prefix='product_save'):
    to_save: str = ['product_title', 'product_photo_id', 'product_description', 'product_price', 'product_display']

