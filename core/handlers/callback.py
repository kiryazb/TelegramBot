from aiogram.types import CallbackQuery, Message
from core.utils.callbackdata import ButtonsInfo
from core.handlers import payments
from core.handlers.basic import get_personal_account

from core.utils.dbconnect import Request

from aiogram.fsm.context import FSMContext


async def select_buttons(call: CallbackQuery, callback_data: ButtonsInfo, state: FSMContext, request: Request):
    data = callback_data.number
    if data == '1':
        await payments.get_form(call.message, state)
    if data == "main_menu":
        user_id = call.from_user.id
        await get_personal_account(call.message, request, user_id)
