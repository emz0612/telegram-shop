import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("TOKEN")  # گرفتن توکن از محیط اجرا
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("سلام! به ربات فروشگاهی خوش آمدید.")

if __name__ == '__main__':
    executor.start_polling(dp
