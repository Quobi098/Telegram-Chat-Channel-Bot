from aiogram.types import ContentType

from loader import dp
from aiogram import types

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def pdf_handler(message: types.document):
    await message.answer({message.document.mime_type})