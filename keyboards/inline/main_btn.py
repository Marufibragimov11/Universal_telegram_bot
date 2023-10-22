from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕Foyda", callback_data="income"),
            InlineKeyboardButton(text="➖Xarajat", callback_data="outcome"),
        ],
        [
            InlineKeyboardButton(text="💵Statistika", callback_data="statistics"),
        ],
        [
            InlineKeyboardButton(text="⬇️Instagramdan yuklash", callback_data="insta_save"),
            InlineKeyboardButton(text="⬇️YouTubedan yuklash", callback_data="yt_save"),
        ],
    ],
)

months_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yanvar", callback_data="January"),
            InlineKeyboardButton(text="Fevral", callback_data="February"),
        ],
        [
            InlineKeyboardButton(text="Mart", callback_data="March"),
            InlineKeyboardButton(text="Aprel", callback_data="April"),
        ],
        [
            InlineKeyboardButton(text="May", callback_data="May"),
            InlineKeyboardButton(text="Iyun", callback_data="June"),
        ],
        [
            InlineKeyboardButton(text="Iyul", callback_data="July"),
            InlineKeyboardButton(text="Avgust", callback_data="August"),
        ],
        [
            InlineKeyboardButton(text="Sentyabr", callback_data="September"),
            InlineKeyboardButton(text="Oktyabr", callback_data="October"),
        ],
        [
            InlineKeyboardButton(text="Noyabr", callback_data="November"),
            InlineKeyboardButton(text="Dekabr", callback_data="December"),
        ],
        [
            InlineKeyboardButton(text="🏠Menu", callback_data="menu"),
        ],
    ],
)

detailed_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📋Batafsil Ma'lumot", callback_data="all_details"),
        ],
        [
            InlineKeyboardButton(text="🏠Menu", callback_data="menu"),
        ],
    ],
)

