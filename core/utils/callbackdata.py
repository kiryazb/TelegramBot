from aiogram.filters.callback_data import CallbackData


class ButtonsInfo(CallbackData, prefix="button"):
    number: str