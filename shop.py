import asyncio
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import CommandStart,Command
import logging
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

API_TOKEN = '7700996038:AAFJjU3dhffC2f4fXxxIJ3btT7wKNCnnYho'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s-% (levelname)s-%(name)s-% (message)s'
)

bot = Bot(API_TOKEN)

kb = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='hello')]
    ],
    resize_keyboard=True
)



dp = Dispatcher()



@dp.message(CommandStart())
async def start(message: types.Message):
     await message.answer('Привет я телеграмм бот магазина \nесли интересует найк /nike \nесли интересует адидас /adidas \nесли интересует луи витон /lui_viton',reply_markup=kb)

@dp.message(F.text =='hello')
async def start(message: types.Message):
    await message.answer('hello')

@dp.message(Command('nike'))
async def echo(message: types.Message):
    await message.answer_photo('https://sportive.akinoncdn.com/products/2022/08/11/394117/f3fdb577-eda5-4559-92a7-34369678ba8d_size1400x1400_quality100.jpg',
    caption = 'nike \nцена: 15000 сом. \nкупить : /buy')
    # await message.answer('nike new line \nцена: 10000 сом.') #
    await message.answer_photo('https://24.kg/thumbnails/18081/e7936/102036_w750_h_r.jpg',
                                caption = 'nike sb dunk \nцена: 15000 сом. \n купить : /buy') #
    await message.answer_photo('https://nikitaefremov.ru/upload/resize_cache/iblock/a98/fx8qxsk9lm3rr11ibhwrav8706sodlqw/515_384_1/cb527828_15c2_11ef_9afe_3cecef222b53_5c2d32e6_5931_11ef_9d11_3cecef222b53.png',
                                caption = 'nike waffle \nцена: 9000 сом.\n купить : /buy') #
    
    await message.answer('если интересует найк /nike \nесли интересует адидас /adidas \nесли интересует луи витон /lui_viton')
    

@dp.message(Command('adidas'))
async def echo(message: types.Message):
    await message.answer_photo('https://hadi.ua/image/catalog/1novosti/skolko-stoyat-krossovki-adidas-muzhskie-1-hadi.ua.jpg', 
                               caption = 'adidas new line \nцена: 12000 сом.')
    await message.answer_photo('https://ir.ozone.ru/s3/multimedia-b/c1000/6644268119.jpg',
                               caption = 'adidas air \nцена: 9599 сом.')
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDywUjX-UnPzBKJWAo3D0qzR80AfPK3_1S_g&s',
                               caption = 'adidas abdullokh \nцена: 16000 сом.')
    
    await message.answer('если интересует найк /nike \nесли интересует адидас /adidas \nесли интересует луи витон /lui_viton')

@dp.message(Command('lui_viton'))
async def echo(message: types.Message):
    await message.answer_photo('https://ir.ozone.ru/s3/multimedia-2/6577376534.jpg', 
                               caption = 'lui viton air \nцена: 13999сом.')  
    await message.answer_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMMWiub5iTZBMAKpRzzOx5Z9N2FBseW50g1Q&s',
                               caption = 'lui viton new \nцена: 20000сом.')    
    await message.answer_photo('https://твои-кроссовки.рф/wp-content/uploads/2023/08/dsc_0794.jpg',
                               caption = 'lui viton abdullokh \nцена: 23990 сом.')
    await message.answer('если интересует найк /nike \nесли интересует адидас /adidas \nесли интересует луи витон /lui_viton')  

@dp.message(Command('buy'))
async def echo(messege: types.Message):
    await messege.answer_photo('https://play-lh.googleusercontent.com/Byl6BHzEv7tWDGa5QUgztneq8C8TGYelu8ywVMTTRUH2e9keboyLqL4YhmzaU3vjgA')
    await messege.answer('перевидите на этот номер ')

async def echo(message: types.Message):
    await message.answer('введите адрес и город')
    await message.answer('успсшный заказ мы доставим через 10 дней')
@dp.message()
async def echo(message: types.Message):
    await message.answer("павыф")

async def main():
    logging.info('ваш бот запушен')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

