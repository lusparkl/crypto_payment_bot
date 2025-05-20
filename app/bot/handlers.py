from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import app.bot.utils as utls

rt = Router()

@rt.message(Command("start"))
async def welcome_message(message: types.Message):
    await message.answer(text=utls.start_menu_text, reply_markup=utls.start_menu_markup.as_markup(), parse_mode="MarkdownV2")