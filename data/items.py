from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.item import Item

Hyundai_Tucson = Item(
    title="Hyundai Tucson",
    description="Hyundai Tucson - компактный кроссовер корейской компании Hyundai. "
                "Называется по имени города Тусон в штате Аризона, США.",
    currency="RUB",
    prices=[LabeledPrice(label="Hyundai Tucson", amount=1000_00)],
    start_parameter="create_invoice_hyundai_tucson",
    photo_url="https://sportishka.com/uploads/posts/2022-08/1660869064_16-sportishka-com-p-mashina-khendai-tussan-novii-krasivo-foto-21.jpg",
    photo_size=600
)

Hyundai_Sonata = Item(
    title="Hyundai Sonata",
    description="Hyundai Sonata — среднеразмерный переднеприводной седан.",
    currency="RUB",
    prices=[LabeledPrice(label= "Hyundai Sonata", amount=1000_00),
            LabeledPrice(label="Доставка", amount=1000_00),
            LabeledPrice(label="Скидка", amount=-1000_00),
            LabeledPrice(label="НДС", amount=1000_00)],
    start_parameter="create_invoice_hyundai_sonata",
    photo_url="https://i.pinimg.com/originals/89/27/74/8927743ed309fe220426999c35af46a4.jpg",
    photo_size=600,
    need_shipping_address=True,
    is_flexible=True
)

POST_REGULAR_SHIPPING = types.ShippingOption(id="post_reg", title="Почтой",
                                             prices=[types.LabeledPrice("Обычная коробка", 1000_00),
                                                     types.LabeledPrice("Почтой обычной", 1000_00)])

POST_FAST_SHIPPING = types.ShippingOption(id="post_fast", title="Почтой (VIP)",
                                          prices=[types.LabeledPrice("Супер прочная коробка", 1000_00),
                                                  types.LabeledPrice("Почтой срочной - DHL (3 дня)", 1000_00)])

PICKUP_SHIPPING = types.ShippingOption(id="pickup", title="Самовывоз",
                                       prices=[types.LabeledPrice("Самовывоз из магазина", -1000_00)])