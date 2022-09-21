import logging
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hey dude!\n I'm bot created for sweetheart Uluyaner.\nI remaind to take pills")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)