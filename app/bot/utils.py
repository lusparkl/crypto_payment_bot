from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

start_menu_text = (
    "🚀 *Welcome to the Access Bot\\!*\n\n"
    "Here you can unlock *exclusive access* to our private Telegram channel by making a *one\\-time crypto payment*\\. "
    "No subscriptions, no hassle — just pay once and you\\'re in\\.\n\n"
    "💰 *Available tokens:*\n"
    "🔹 USDT \\(TRC20, ERC20, SOL\\)\n"
    "🔹 SOL\n"
    "🔹 ETH\n\n"
    "🔐 Once your payment is confirmed, you'll instantly receive a *private invite link* to join\\.\n\n"
    "To begin, tap the button below and choose your preferred payment option 👇"
)

start_menu_markup=InlineKeyboardBuilder()
usdt_button=InlineKeyboardButton(text="💸 Pay with USDT", callback_data="usdt")
sol_button=InlineKeyboardButton(text="⚡ Pay with SOL", callback_data="sol  ")
eth_button=InlineKeyboardButton(text="🪙 Pay with ETH", callback_data="eth")
start_menu_markup.add(usdt_button, sol_button, eth_button)