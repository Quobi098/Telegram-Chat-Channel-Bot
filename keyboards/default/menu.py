from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ru_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти слово в PDF файле")
        ],
        [
            KeyboardButton(text="Информация о файле")
        ],
        [
            KeyboardButton(text="Выбрать язык")
        ]
    ],
    resize_keyboard=True
)

eng_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Find word in PDF file")
        ],
        [
            KeyboardButton(text="Information about file")
        ],
        [
            KeyboardButton(text="Choose language")
        ]
    ],
    resize_keyboard=True
)