import asyncio
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import CommandStart,Command

API_TOKEN = '8446148065:AAGFOJJO9cwS2gZ0jlDHcsv7ozV97JH9fKs'


bot = Bot(API_TOKEN)


dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привут я телеграмм бот напишите /register что бы пройти регистрацию')

@dp.message(Command('register'))
async def echo(message: types.Message):
    await message.answer('введите имя \nвведите фамилию \nвведите номер \nвведите имаел')

@dp.message()
async def echo(message: types.Message):
    await message.answer('успешная регистрация')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

