from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("menu", "Меню команд"),
        types.BotCommand("test", "Пройти тест"),
        types.BotCommand("set_photo", "Установить фото в группе"),
        types.BotCommand("set_title", "Установить название группы"),
        types.BotCommand("set_description", "Установить описание группы"),
        types.BotCommand("ro", "Режим Read Only"),
        types.BotCommand("unro", "Отключить RO"),
        types.BotCommand("ban", "Забанить"),
        types.BotCommand("unban", "Разбанить"),
        types.BotCommand("channels", "Список каналов на подписку"),
        types.BotCommand("create_post", "Предложить пост в канале"),
        types.BotCommand("get_cat", "Прислать кота"),
        types.BotCommand("more_cats", "Прислать больше котов")
    ])
