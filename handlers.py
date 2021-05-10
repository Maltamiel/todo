from app import bot, dp
from aiogram.types import Message
from config import admin_id, todo, HELP

import time

uDate, uTask = 0, 0
reqv= 0
"""
0 - ожидание команды
1 - ожидание даны
2 - ожидание задачи
"""


async def send_to_admin(dp):
  await bot.send_message(chat_id=admin_id, text="BOT EST")

@dp.message_handler(commands = ["start"])
async def start(message:Message):
  await message.answer(text="ROBOT RABOTAT")

@dp.message_handler(commands = ["add"])
async def add(message:Message):
  global reqv
  await message.answer(text="add")
  reqv = 1

@dp.message_handler(commands = ["done"])
async def done(message:Message):
  await message.answer(text="done")

@dp.message_handler(commands = ["show"])
async def show(message:Message):
  for date in sorted( todo.keys() ):
    for task in todo[ date ]:
       await message.answer(text=f"[{date}] - {task}")

@dp.message_handler(commands = ["help"])
async def help(message:Message):
  await message.answer(text="help")

@dp.message_handler()
async def echo(message:Message):
 global reqv, uDate, uTask, todo
 if reqv == 1:
   uDate = message.text
   try:
     time.strptime(uDate, "%d.%m.%Y") #12.02.2021
   except ValueError:
    await message.answer(text = "ne verno")
    reqv = 0
    return
   await message.answer(text = "CHTO DELAT")
   reqv = 2
 elif reqv = 2:
   uTask = message.text
   if uDate in todo:
     todo[ uDate ].append( uTask )
   else:
     todo[ uDate ] = [ uTask ] 
   await message.answer(f"Added task "{uTask}" in "{uDate}"")
   reqv = 0
   