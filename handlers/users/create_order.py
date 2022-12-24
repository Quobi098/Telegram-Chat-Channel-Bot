from aiogram import types
from aiogram.dispatcher.filters import Command

from data.items import Hyundai_Sonata, Hyundai_Tucson, POST_FAST_SHIPPING, POST_REGULAR_SHIPPING, PICKUP_SHIPPING
from loader import dp, bot


@dp.message_handler(Command("invoices"))
async def show_invoices(message: types.Message):
    await bot.send_invoice(message.from_user.id,
                           **Hyundai_Sonata.generate_invoice(),
                           payload="123456")
    await bot.send_invoice(message.from_user.id,
                           **Hyundai_Tucson.generate_invoice(),
                           payload="123457")

@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code == "KZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[
                                            POST_FAST_SHIPPING,
                                            POST_REGULAR_SHIPPING,
                                            PICKUP_SHIPPING
                                        ], ok=True)

    elif query.shipping_address.country_code == "US":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Сюда не доставляем")

    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[POST_REGULAR_SHIPPING],
                                        ok=True)

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id,
                                        ok=True)