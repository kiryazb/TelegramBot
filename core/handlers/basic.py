from aiogram.types import Message
from aiogram.filters import CommandObject

from core.keyboards.reply import reply_keyboard
from core.keyboards.inline import get_inline_keyboard

from parser.main import parser

from core.utils.dbconnect import Request


async def get_start(message: Message, request: Request):
    await request.add_data(message.from_user.id, message.from_user.username, message.from_user.first_name,
                           0, 0)
    await message.answer(f"""<b>Добро пожаловать, {message.from_user.first_name}!
                            🔹Бот готов к использованию.
                            🔹<a href="https://t.me/xdxd_vou">Свяжись со мной</a>
                            🔹Спасибо, что решили воспользоваться нашим сервисом.</b>""", parse_mode="HTML",
                         reply_markup=reply_keyboard)


async def get_personal_account(message: Message, request: Request, user_id=None):
    if user_id:
        result_list = await request.get_info(user_id)
    else:
        result_list = await request.get_info(message.from_user.id)
    for result in result_list:
        await message.answer(f"""👤 Пользователь: @{result["user_name"]}
                                🪪 ID: {result["user_id"]}
                                💰 Баланс: {result["balance"]} ₽
                                📊 Количество покупок: {result["purchase_count"]}""", reply_markup=get_inline_keyboard())


async def buy_parser(message: Message, request: Request):
    await message.answer("Стоимость парсера - 50 рублей")
    result = await request.get_balance(message.from_user.id)
    if result - 50 > 0:
        await message.answer("Парсер приобретен✅")
        await request.decreased_balance(50, message.from_user.id)
        product = await parser()
        for i in product:
            await message.answer(f"{i[0]} {i[1]}")
    else:
        await message.answer("Недостаточно средств")
