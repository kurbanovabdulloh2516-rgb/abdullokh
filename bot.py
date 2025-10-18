import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "8071873387:AAFVM4JOpqhrj6RiQwWd9TR6HRUr2ohHF1w"
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Простой каталог
PRODUCTS = [
    ("mug", "Кружка", 500),
    ("shirt", "Футболка", 1500),
    ("sticker", "Стикер", 100),
]


carts = {}

# --- старт: каталог ---
@router.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardBuilder()
    for pid, title, price in PRODUCTS:
        kb.button(
            text=f"{title} - {price}₽",
            callback_data=f"add:{pid}"
        )
    kb.button(text="🛒 Корзина", callback_data="cart")
    kb.adjust(1)
    await message.answer("Наш магазин:", reply_markup=kb.as_markup())

# --- добавление товара ---
@router.callback_query(F.data.startswith("add:"))
async def add_item(callback: CallbackQuery):
    pid = callback.data.split(":")[1]
    user_id = callback.from_user.id
    carts.setdefault(user_id, []).append(pid)
    await callback.answer("Добавлено!")

# --- просмотр корзины ---
@router.callback_query(F.data == "cart")
async def show_cart(callback: CallbackQuery):
    user_id = callback.from_user.id
    items = carts.get(user_id, [])
    if not items:
        await callback.message.answer("Корзина пуста")
        await callback.answer()
        return

    # Собираем текст корзины
    text = "В корзине:\n"
    for pid in items:
        for id2, title, price in PRODUCTS:
            if id2 == pid:
                text += f"- {title} ({price}₽)\n"
    await callback.message.answer(text)
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
