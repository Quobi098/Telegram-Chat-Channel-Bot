from aiogram import types

from loader import dp

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def bot_voice(message: types.Voice):
    chat_id = message.chat.id

    from loader import bot

    await bot.send_message(chat_id, "Пошел в жопу со своим аудио")
