from aiogram.dispatcher.filters import Command
from aiogram.types import Message, InputFile, MediaGroup, ContentType
from loader import dp, bot


# @dp.message_handler(content_types=ContentType.PHOTO)
# async def get_file_id_p(message: Message):
#     await message.reply(message.photo[-1].file_id)
#
#
# @dp.message_handler(content_types=ContentType.VIDEO)
# async def get_file_id_v(message: Message):
#     await message.reply(message.video.file_id)


@dp.message_handler(Command("get_cat"))
async def send_cat(message: Message):
    photo_file_id = "AgACAgIAAxkBAAIEf2OTXh-t571-g6UauynMJoST9TesAAK6xDEb5LqYSPYrM-VEUa5iAQADAgADeAADKwQ"
    photo_url = "https://i.pinimg.com/originals/ad/12/e9/ad12e94bcd94e609bc176a239c29642e.jpg"
    photo_bytes = InputFile(path_or_bytesio="photos/cat.jpg")
    await message.answer_photo(photo=photo_url,
                         caption="Вот тебе фотка кота /more_cats")
    # await message.answer_video("BAACAgIAAxkBAAIEkGOTbqr4vRAQsb3eWH5AHWuTMIglAAIMIgACGWmhSFkRgKfRtg1OKwQ")


@dp.message_handler(Command("more_cats"))
async def more_cats(message: Message):
    album = MediaGroup()
    photo_url = "https://minimanual.com/wp-content/uploads/2020/08/gato-naranja-4.jpg"
    photo_file_id = "AgACAgQAAxkBAAIEhGOTXsxTl5CayN6wM2EhxGi29-c4AAL-rTEbL_NFUgPevDMteabLAQADAgADdwADKwQ"
    photo_bytes = InputFile(path_or_bytesio="photos/cat.jpg")
    video_file_id = "BAACAgIAAxkBAAIEkGOTbqr4vRAQsb3eWH5AHWuTMIglAAIMIgACGWmhSFkRgKfRtg1OKwQ"
    album.attach_photo(photo_file_id)
    album.attach_photo(photo_bytes)
    album.attach_photo(photo_url)
    album.attach_video(video=video_file_id, caption="Видео где котик запрыгивает на кровать")
    await message.answer_media_group(media=album)
