from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import ButtonsInfo


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Пополнить баланс", callback_data=ButtonsInfo(number='1'))
    keyboard_builder.button(text="Мои карты", callback_data=ButtonsInfo(number='2'))
    keyboard_builder.button(text="Мои аккаунты", callback_data=ButtonsInfo(number='3'))
    keyboard_builder.button(text="Программы лояльности", callback_data=ButtonsInfo(number='4'))

    keyboard_builder.adjust(1, 2, 1)
    return keyboard_builder.as_markup()


def back_to_menu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="ℹ️В главное меню", callback_data=ButtonsInfo(number='main_menu'))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
