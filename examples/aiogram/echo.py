import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import tg_token, proxy
import sys

if not tg_token:
    print("Enter Telegram token to 'config.py' file...")
    sys.exit()
if proxy:
    bot = Bot(token=tg_token, proxy=proxy)
else:
    bot = Bot(token=tg_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def send_welcome(message: types.Message):
    await message.reply(message.text, reply=False)

executor.start_polling(dp, skip_updates=True)