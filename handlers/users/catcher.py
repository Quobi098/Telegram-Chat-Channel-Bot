from loader import dp
from aiogram import types


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def catch_doc(message: types.Message):
    await message.document.download()
    await message.reply("Документ скачан\n"
                         f"<pre>FILE ID = {message.document.file_id}</pre>",
                         parse_mode="HTML")

@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def catch_audio(message: types.Message):
    await message.audio.download()
    await message.reply("Аудио скачан\n"
                         f"<pre>FILE ID = {message.audio.file_id}</pre>",
                         parse_mode="HTML")

@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def catch_video(message: types.Message):
    await message.video.download()
    await message.reply("Видео скачан\n"
                         f"<pre>FILE ID = {message.video.file_id}</pre>",
                         parse_mode="HTML")

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def catch_photo(message: types.Message):
    await message.photo[-1].download()
    await message.reply("Фото скачан\n"
                         f"<pre>FILE ID = {message.photo[-1].file_id}</pre>",
                         parse_mode="HTML")

# @dp.message_handler(content_types=types.ContentTypes.ANY)
# async def catch_any(message: types.Message):
#     await message.reply(f"Вы прислали... {message.content_type}")