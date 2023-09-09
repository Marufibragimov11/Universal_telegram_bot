from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👥Foydalanuvchilar'),
            KeyboardButton(text='🎁Reklama yuborish'),
        ],
    ],
    resize_keyboard=True
)