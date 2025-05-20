from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import app.bot.utils as utls
from db.db import Database

rt = Router()

@rt.message(Command("start"))
async def welcome_message(message: types.Message):
    db = Database()
    if not db.is_user_exists(message.from_user.id):
        db.add_user(user_id=message.from_user.id, username=message.from_user.username)

    await message.answer(text=utls.start_menu_text, reply_markup=utls.start_menu_markup.as_markup(), parse_mode="MarkdownV2")

