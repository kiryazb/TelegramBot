from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="💲 Купить"),
        KeyboardButton(text="🛒 Товары"),
        ],
    [
        KeyboardButton(text="ℹ️ Личный кабинет")
        ],
    [
        KeyboardButton(text="💬 Помощь"),
        ]
], resize_keyboard=True
)