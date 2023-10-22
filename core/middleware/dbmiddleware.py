from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Dict, Callable, Any, Awaitable
from core.utils.dbconnect import Request
import asyncpg


class DbSession(BaseMiddleware):
    def __init__(self, connector: asyncpg.pool.Pool) -> None:
        super().__init__()
        self.connector = connector

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        async with self.connector.acquire() as connect:
            data['request'] = Request(connect)
            return await handler(event, data)