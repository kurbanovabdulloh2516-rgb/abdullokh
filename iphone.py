import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "8071873387:AAFVM4JOpqhrj6RiQwWd9TR6HRUr2ohHF1w"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
r = Router()
dp.include_router(r)

Phone = {
    "iphone_17": ("iPhone 17", "https://img.jabko.ua/image/cache/catalog/products/2025/09/100924/17proCosmic_Orange-1-420x420.png.webp", 155000),
    "iphone_16": ("iPhone 16", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9ZVKUn1_yjBl-C5zh5iMrOX1NWlTgW9tN-w&s", 130000),
    "iphone_15": ("iPhone 15", "https://asiastore.kg/image/cache/catalog/iphone/iphone15/1515%2B/iphone15/black/iphone151-1200x1200.jpg", 110000),

    "samsung_s25": ("Samsung S25 Ultra", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtayoLGeX2Kg15Fg9SncD6J_fxKIKQVAzJ_A&s", 160000),
    "samsung_s24": ("Samsung S24 Ultra", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcKhgf_RZA-0oYb_FcpZCf1LvKV-7rXfk12w&s", 120000),
    "samsung_s23": ("Samsung S23 Ultra", "https://i5.walmartimages.com/seo/Samsung-Galaxy-S23-Ultra-5G-SM-S918U1-1024GB-Green-US-Model-Factory-Unlocked-Cell-Phone-Very-Good-Condition_f79cd206-c28d-4ccf-8f97-91710d49e920.b4e45ca2092a3769bf8842ef96ec25e4.jpeg", 95000),

    "xiaomi_14": ("Xiaomi 14", "https://login.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2014/3-500x400.jpg", 30000),
    "xiaomi_13": ("Xiaomi 13", "https://login.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2013/xiaomi%2013-500x400.jpg", 24999),
    "xiaomi_12": ("Xiaomi 12", "https://login.kg/image/cache/catalog/new/Phones/Xiaomi/Xiaomi%2012%20Pro/3-500x400.jpg", 35000),
}

def phone_menu():
    kb = InlineKeyboardBuilder()
    for pid, (name, _, _) in Phone.items():
        kb.button(text=name, callback_data=f"phone:{pid}")
    kb.adjust(1)
    return kb.as_markup()

@r.message(CommandStart())
async def start(m: Message):
    await m.answer("📱 Выбери смартфон:", reply_markup=phone_menu())

@r.callback_query(F.data.startswith("phone:"))
async def show_phone(c: CallbackQuery):
    _, pid = c.data.split(":")
    name, url, price = Phone[pid]
    await c.answer()
    await c.message.answer_photo(
        url,
        caption=f"{name}\n💰 Цена: {price:,} сом.",
    )

async def main():   
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
