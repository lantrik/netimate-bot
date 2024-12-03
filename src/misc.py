from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.core.bot import Bot
from src.core.bot import Bot
from src.core.logger import setup as logger_setup
from src.ext.schedulers.cache_cleaner import cache_cleaner


scheduler = AsyncIOScheduler()
bot = Bot()

def _schedule_interval_jobs():
    scheduler.add_job(cache_cleaner, 'interval', hours=1)

async def setup():
    logger_setup()
    _schedule_interval_jobs()

    bot.load_routers()
    
    await bot.run()