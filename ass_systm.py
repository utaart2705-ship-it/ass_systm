
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

import asyncio

API_TOKEN = "8691718321:AAHxq02I5W7IvxKRGYORMdoo0hhQL4hKh8U"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start command
@dp.message(Command(commands=["start"]))
async def cmd_start(message: Message):
    await message.answer("I will help you clean hidden spam in your group ")

# /help command
@dp.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer("If you have any problem, please write it down. I will send it to the administrator, and you will get a reply within 24 hours.")
# Botni ishga tushurish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
