from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.default import ru_menu, eng_menu
from keyboards.inline import choice
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите опцию из меню ниже", reply_markup=ru_menu)

@dp.message_handler(text="Найти слово в PDF файле")
async def ru_find_button(message: types.Message):
    await message.answer("Отправьте слово, которое нужно найти в файле", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Информация о файле")
async def ru_info_button(message: types.Message):
    await message.answer("Файл содержит 50 страниц и 5000 знаков", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Выбрать язык")
async def ru_lang_button(message: types.Message):
    await message.answer("Выберите удобный вам язык", reply_markup=choice)



@dp.message_handler(text="Find word in PDF file")
async def eng_find_button(message: types.Message):
    await message.answer("Send the word, which i need to find in file", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Information about file")
async def eng_info_button(message: types.Message):
    await message.answer("File contain 50 pages and 5000 characters", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Choose language")
async def eng_lang_button(message: types.Message):
    await message.answer("Choose comfortable language for you", reply_markup=choice)


@dp.callback_query_handler(text='Ru')
async def eng_find_button(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Выбранный язык: Русский", reply_markup=ru_menu)

@dp.callback_query_handler(text='Eng')
async def eng_find_button(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Chosen language: English", reply_markup=eng_menu)