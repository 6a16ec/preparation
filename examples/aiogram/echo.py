import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import tg_token, proxy, proxy_auth

logging.basicConfig(level=logging.INFO)
bot = Bot(token=tg_token) if proxy is None else \
Bot(token=tg_token, proxy=proxy) if proxy_auth is None else \
Bot(token=tg_token, proxy=proxy, proxy_auth=proxy_auth)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def send_welcome(message: types.Message):
    await message.reply(message.text, reply=False)

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
