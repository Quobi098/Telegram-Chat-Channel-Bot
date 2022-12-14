from aiogram import types
from loader import dp


# @dp.message_handler(content_types=types.ContentTypes.TEXT)
# async def bot_echo(message: types.Message):
#     # await message.answer(message.text)
#
#     chat_id = message.chat.id
#     text = message.text
#
#     from loader import bot
#
#     await bot.send_message(chat_id=chat_id, text=text)
#
#     # await message.reply(text)
#     # await message.answer(text)
