from aiogram.types import Message
from aiogram.filters import Filter

from src.config import DEVELOPER_ID


class DeveloperFilter(Filter):
    """Filter for the bot developer"""
    async def __call__(self, message: Message) -> bool:
        return (message.from_user.id == DEVELOPER_ID)
