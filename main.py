import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from decouple import config

#add  logging in bot
logging.basicConfig(level=logging.INFO)
#object bot
bot = Bot(token=config('TOKEN'))
#dispatcher
dp = Dispatcher()

#handler for command /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

#start polling and new update
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
