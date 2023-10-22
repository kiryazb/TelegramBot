import asyncio

import logging

import asyncpg

from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters.command import CommandStart, Command

from core.utils.settings import settings
from core.handlers.basic import get_start, get_personal_account, buy_parser
from core.handlers import payments
from core.utils.dbconnect import Request

from core.handlers.callback import select_buttons
from core.utils.callbackdata import ButtonsInfo

from core.middleware.dbmiddleware import DbSession

from core.utils.statespayment import StepsForm


async def create_db():
    try:
        pool_connect = await asyncpg.create_pool(user="postgres", password="postgres", host="127.0.0.1",
                                                 port=5432, command_timeout=60)
        request = Request(pool_connect)
        await request.create_database()
    except asyncpg.exceptions.DuplicateDatabaseError:
        return -1
    except Exception as e:
        print(f"Error: {e}")


async def create_table(pool_connect):
    request = Request(pool_connect)
    await request.create_table()


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    await create_db()

    pool_connect = await asyncpg.create_pool(user="postgres", password="postgres", database="users_big_project",
                                             host="127.0.0.1", port=5432, command_timeout=60)

    await create_table(pool_connect)

    bot = Bot(token=settings.bot.bot_token)

    dp = Dispatcher()

    dp.update.middleware.register(DbSession(pool_connect))
    dp.message.register(get_start, CommandStart())
    dp.callback_query.register(select_buttons, ButtonsInfo.filter())

    dp.message.register(get_personal_account, F.text == "ℹ️ Личный кабинет")
    dp.message.register(buy_parser, F.text == "💲 Купить")

    dp.message.register(payments.get_form, F.data == "1")
    dp.message.register(payments.check_sum, StepsForm.GET_SUM)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
