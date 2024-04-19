from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN = '7061005848:AAGi53xx05J6azdy_Dszyjai7TMRPeowda0'

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage = storage)
