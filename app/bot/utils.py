from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

start_menu_text = r"""
👋 *Welcome\!*

To get **access** to the private channel, please make a *one\-time crypto payment* using the link below 👇

🔐 After successful payment, you will receive **instant access** to the channel\.  

*Supported:*
🪙 BTC, ETH, USDT, TON, SOL, and more\!

_Thank you for your support\!_
"""

start_menu_markup=InlineKeyboardBuilder()
pay_btn=InlineKeyboardButton(text="Start payment", callback_data="pay")
start_menu_markup.add(pay_btn)

payment_menu_text =r"""
💳 *How to Pay in 3 Simple Steps:*

1️⃣ Click the link below to open the payment page:  
💸 [Click here to pay](https://nowpayments.io/payment/?iid=6002521710)

2️⃣ After opening the page, copy the `Payment ID` as shown on the screenshot\.  
You will need to send it here to confirm your payment\.

3️⃣ Complete the payment on the website using your preferred crypto\.

🚀 Once your payment is confirmed, you'll automatically gain access to the private channel\.
"""