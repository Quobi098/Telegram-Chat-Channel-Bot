import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PROVIDER_TOKEN = str(os.getenv("PROVIDER_TOKEN"))

admins = [
    1175657579
]
allowed_users = [

]

channels = ["@demo_test_tg"]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
