from aiogram.types import ChatAdministratorRights

from src.core.bot import Bot
from src.core.logger import setup as logger_setup


bot = Bot()

async def setup():
    logger_setup()

    bot.load_routers()
    await bot.run()