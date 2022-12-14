from aiogram.types import InlineKeyboardMarkup, inline_keyboard, callback_query, InlineKeyboardButton

check_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Проверить подписки",
                                 callback_data="check_subs")
        ]
    ]
)