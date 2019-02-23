import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import tg_token, proxy
import sys

DELAY = 1

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


async def update_price():
    print("Hello World")

def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, update_price, loop)
    executor.start_polling(dp, loop=loop, skip_updates=True)