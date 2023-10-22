from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statespayment import StepsForm
from core.utils.dbconnect import Request

from core.keyboards.inline import back_to_menu


async def get_form(message: Message, state: FSMContext):
    await message.answer("Введите сумму для пополнения: ")
    await state.set_state(StepsForm.GET_SUM)


async def check_sum(message: Message, state: FSMContext, request: Request):
    if not(message.text.isdigit()) or int(message.text) <= 0:
        await message.answer("Некорректная сумма")
    else:
        await message.answer(f"Ты пополнил баланс на:{message.text}", reply_markup=back_to_menu())
        await request.add_balance(message.text, message.from_user.id)
        await state.clear()
