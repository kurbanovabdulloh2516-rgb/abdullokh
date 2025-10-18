import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "8071873387:AAFVM4JOpqhrj6RiQwWd9TR6HRUr2ohHF1w"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Список товаров
PRODUCTS = {
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

# Корзины пользователей
carts = {}

# 📱 Главное меню: список товаров с кнопками
@router.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardBuilder()
    for pid, (title, _, price) in PRODUCTS.items():
        kb.button(
            text=f"{title} - {price:,} сом",
            callback_data=f"phone:{pid}"
        )
    kb.button(text="🛒 Корзина", callback_data="cart")
    kb.adjust(1)
    await message.answer("📱 Добро пожаловать! Выбери товар:", reply_markup=kb.as_markup())

# 📸 Показать фото товара и кнопку добавить в корзину
@router.callback_query(F.data.startswith("phone:"))
async def show_phone(callback: CallbackQuery):
    pid = callback.data.split(":")[1]
    name, url, price = PRODUCTS[pid]

    kb = InlineKeyboardBuilder()
    kb.button(text="Добавить в корзину 🛒", callback_data=f"add:{pid}")
    kb.adjust(1)

    await callback.message.answer_photo(
        photo=url,
        caption=f"{name}\n💰 Цена: {price:,} сом",
        reply_markup=kb.as_markup()
    )
    await callback.answer()

# ➕ Добавить товар в корзину
@router.callback_query(F.data.startswith("add:"))
async def add_item(callback: CallbackQuery):
    pid = callback.data.split(":")[1]
    user_id = callback.from_user.id
    carts.setdefault(user_id, []).append(pid)
    await callback.answer("✅ Товар добавлен в корзину!")

# 🛒 Показать корзину
@router.callback_query(F.data == "cart")
async def show_cart(callback: CallbackQuery):
    user_id = callback.from_user.id
    items = carts.get(user_id, [])

    if not items:
        await callback.message.answer("🛒 Ваша корзина пуста.")
        await callback.answer()
        return

    text = "🛍 В корзине:\n\n"
    total = 0
    for pid in items:
        name, _, price = PRODUCTS[pid]
        text += f"- {name} — {price:,} сом\n"
        total += price

    text += f"\n💰 Итого: {total:,} сом"

    await callback.message.answer(text)
    await callback.answer()

# 🔹 Запуск бота
async def main():
    print("🤖 Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
