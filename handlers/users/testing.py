from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование. \n"
                         "Вопрос №1 \n\n"
                         "Вы часто занимаетесь бессмысленными делами "
                         "(бесцельно блуждаете по интернету, клацаете пультом телевизора, просто смотрите в потолок)?")

    await Test.Q1.set()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer1 = message.text
    await state.update_data(answer1=answer1)

    await message.answer("Вопрос №2 \n\n"
                         "Ваша память ухудшилась и вы помните то, что было давно, но забываете недавние события?")
    await Test.next()
    # await Test.Q2.set()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer2 = message.text
    await state.update_data(answer2=answer2)

    await message.answer("Вопрос №3 \n\n"
                         "Вы бы дружили с самим собой??")
    await Test.next()

@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer3 = message.text
    await state.update_data(answer3=answer3)

    await message.answer("Вопрос №4 \n\n"
                         "У вас есть ощущение, что сегодняшний день уже повторялся сотни раз до этого?")
    await Test.next()

@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer4 = message.text
    await state.update_data(answer4=answer4)

    await message.answer("Вопрос №5 \n\n"
                         "Что в этой жизни вы делаете иначе, чем другие люди?")
    await Test.next()

@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer5 = message.text
    await state.update_data(answer5=answer5)

    await message.answer("Вопрос №6 \n\n"
                         "Если бы счастье стало главной валютой, кем бы вы работали?")
    await Test.next()

@dp.message_handler(state=Test.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    answer6 = message.text
    await state.update_data(answer6=answer6)

    await message.answer("Вопрос №7 \n\n"
                         "Пойти на преступление, чтобы накормить своего голодного ребенка, — это"
                         "плохо или просто необходимо?")
    await Test.next()

# @dp.message_handler(text="Отмена")
# async def cancel_test(message: types.Message, state: FSMContext):
#     await state.reset_state(with_data=False)

@dp.message_handler(state=Test.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    answer7 = message.text

    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = data.get('answer2')
    answer3 = data.get('answer3')
    answer4 = data.get('answer4')
    answer5 = data.get('answer5')
    answer6 = data.get('answer6')

    await message.answer("Спасибо за ваши ответы")
    await message.answer(f"Ответ №1: {answer1}")
    await message.answer(f"Ответ №2: {answer2}")
    await message.answer(f"Ответ №3: {answer3}")
    await message.answer(f"Ответ №4: {answer4}")
    await message.answer(f"Ответ №5: {answer5}")
    await message.answer(f"Ответ №6: {answer6}")
    await message.answer(f"Ответ №7: {answer7}")

    await state.reset_state()
