from filters import IsGroup
from loader import dp, bot
from aiogram import types

@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(m: types.Message):
    members = ", ".join([n.get_mention(as_html=True) for n in m.new_chat_members])
    await m.reply(f"Привет, {members}.")

@dp.message_handler(IsGroup(), content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def banned_member(m: types.Message):

    if m.left_chat_member.id == m.from_user.full_name:
        await m.answer(f"{m.left_chat_member.get_mention(as_html=True)} вышел из чата")
    elif m.from_user.id == (await bot.me).id:
        return
    else:
        await m.answer(f"{m.left_chat_member.full_name} был удален из чата"
                       f"пользователем {m.from_user.get_mention(as_html=True)}")