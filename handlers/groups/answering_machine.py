from loader import dp
from aiogram import types

@dp.message_handler(text="Не план")
async def ru_find_button(message: types.Message):
    await message.answer("Заткнись уже! Достал со своим 'не план, не план'")

@dp.message_handler(text="Баха")
async def ru_find_button(message: types.Message):
    await message.answer("Баха ма? Ол малго")

@dp.message_handler(text="Нуржан")
async def ru_find_button(message: types.Message):
    await message.answer("Нуржан вечный токсик, хотя казыр адам болып бастады")

@dp.message_handler(text="Алмас")
async def ru_find_button(message: types.Message):
    await message.answer("Без Алмаса меня бы тут не было")

@dp.message_handler(text="Нурислам")
async def ru_find_button(message: types.Message):
    await message.answer("Уйленшиш уже Нурислам")

@dp.message_handler(text="Айбар")
async def ru_find_button(message: types.Message):
    await message.answer("Unknown. О нем ходят лишь легенды.")