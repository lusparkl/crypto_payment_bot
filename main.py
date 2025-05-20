import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from app.bot.handlers import rt
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    await bot(DeleteWebhook(drop_pending_updates=True))
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())