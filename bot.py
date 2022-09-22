from curses.ascii import US
from email import message
import logging
import asyncio
import datetime as dt
import json
from re import M
from sqlite3 import adapt
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
data = []

with open('UsersData.json', 'r') as f:
    data = json.load(f)

def dump():
    with open('UsersData.json', 'w') as f:
        json.dump(data, f)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    await message.reply("""Hey dude!
I'm bot created for sweetheart Uluyaner.
I remind to take pills. To use me type command reminder and time to remind '9:00' """)

@dp.message_handler(commands=['reminder'])
async def remind_pills(message: types.Message):
    data.append({'u_id': message.from_user.id,
                 'time': message.text.split()[1]})
    dump()
    print(f"Get task to remind about pills\n{data[-1]}")

    await regular_pill_reminder(data[-1]['u_id'], data[-1]['time'], 1)


async def pill_reminder(u_id, time):
    time = dt.time.fromisoformat(time)
    tmp = dt.datetime.now()
    time_dt = dt.datetime(tmp.year, 
                        tmp.month, 
                        tmp.day if time > dt.time(tmp.hour, tmp.minute) else tmp.day+1, 
                        time.hour, 
                        time.minute)

    await asyncio.sleep((time_dt - dt.datetime.now()).seconds)
    await bot.send_message(u_id, "ТАБЛЕТКИ ПИТЬ ПИТЬ ПИТЬ")


async def regular_pill_reminder(u_id, time, timestep):
    time = dt.time.fromisoformat(time)
    tmp = dt.datetime.now()
    time_dt = dt.datetime(tmp.year, 
                        tmp.month, 
                        tmp.day if time > dt.time(tmp.hour, tmp.minute) else tmp.day+1, 
                        time.hour, 
                        time.minute)
    time_step = dt.timedelta(0, 60*int(timestep))

    while True:
        await pill_reminder(u_id, time_dt.isoformat(' ', "minutes").split()[1])
        time_dt += time_step

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)