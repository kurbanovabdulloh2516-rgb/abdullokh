# import asyncio
# from aiogram import Bot, Dispatcher, types,F
# from aiogram.filters import CommandStart,Command

# API_TOKEN = '8446148065:AAGFOJJO9cwS2gZ0jlDHcsv7ozV97JH9fKs'


# bot = Bot(API_TOKEN)


# dp = Dispatcher()



# @dp.message(CommandStart())
# async def start(message: types.Message):
#     await message.answer('''Превет! Я бот абдуллоx \nесли хотите фото мбаппе \nесли хотите фото роналду \nесли хотите фото месси \nесли хотите фото неймара ''')

# @dp.message(Command('ronaldo'))
# async def echo(message: types.Message):
#     await message.answer_photo('https://w0.peakpx.com/wallpaper/147/917/HD-wallpaper-ronaldo-head-sports-uniform-soceer-cr7-man-united-sport.jpg')

# @dp.message(F.text == 'Роналду')
# async def echo(message: types.Message):
#     await message.answer_photo('https://w0.peakpx.com/wallpaper/147/917/HD-wallpaper-ronaldo-head-sports-uniform-soceer-cr7-man-united-sport.jpg')

# @dp.message(Command('messi'))
# async def echo(message: types.Message):
#     await message.answer_photo('https://i.pinimg.com/736x/f8/00/5e/f8005eb3138843c192fa014920fe8fac.jpg')

# @dp.message(F.text == 'месси')
# async def echo(message: types.Message):
#     await message.answer_photo('https://i.pinimg.com/736x/f8/00/5e/f8005eb3138843c192fa014920fe8fac.jpg')

# @dp.message(Command('neymar'))
# async def echo(message: types.Message):
#      await message.answer_photo('https://i.pinimg.com/736x/a8/97/d6/a897d69ea293a561657be680173c9ef4.jpg')


# @dp.message(F.text == 'неймар')
# async def echo(message: types.Message):
#      await message.answer_photo('https://i.pinimg.com/736x/a8/97/d6/a897d69ea293a561657be680173c9ef4.jpg')


# @dp.message(Command('mbappe'))
# async def echo(message: types.Message):
#     await message.answer_photo('https://a-static.besthdwallpaper.com/kylian-mbappe-real-madrid-transfer-loading-wallpaper-1680x1050-125084_5.jpg')

# @dp.message(F.text == 'мбаппе')
# async def echo(message: types.Message):
#     await message.answer_photo('https://a-static.besthdwallpaper.com/kylian-mbappe-real-madrid-transfer-loading-wallpaper-1680x1050-125084_5.jpg')


# @dp.message()
# async def echo(message: types.Message):
#     await message.answer('Не корректный ввод данных')

# async def main():
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())