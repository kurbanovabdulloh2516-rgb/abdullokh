import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "8460613896:AAGP9nzMLKBF7ZFHPnAFiIO9EyOzt_F0Ejw"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)


PRODUCTS = {
    
    "sandvich": ("тойбосс кетчуп", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQH5bJVJm1GpgosEFZhLQsNTV_S1m2X5pyoIQ&s", 80),
    "sandvich_1": ("тойбосс маинез", "https://static.tildacdn.one/tild6632-6230-4332-b833-343664386465/Group_69.png", 85),
    "sandvich_2": ("тойбосс курица", "https://static.tildacdn.one/tild3765-3364-4233-b966-646436363037/Group_67.png", 90),

    "drink": ("pepsi", "https://cdn.ime.by/UserFiles/images/catalog/Goods/0456/00690456/norm/00690456.n_1.png?s=1000x1000", 85),
    "drink_1": ("coca cola", "https://halitlar.com/file/foodsbeverages/coca-cola-original-plastic-bottle-15-l", 90),
    "drink_2": ("fanta", "https://img.vkusvill.ru/pim/images/site_LargeWebP/b5b9e8d9-fecd-4843-a97b-6e791dd6c93a.webp?1672035956.1897", 90),

    "lays": ("Лайс с сыром", "https://lh5.googleusercontent.com/proxy/O47d4dNegPXY7ONh-59B7bxFFy7E1FOKf05ywxFrZGH2SjOjtlCulVQOABohnKrRDXqy61r9Iw0nX0--Csm7iaFpYm0zxo_OkEKVPsJ12qwnblRDdNpNaHovAteTmWw6PNMFCJXcEJ7NvFhVQZzlA5k1VsE8vg0C6s0TaanJQFUUIauhq6MZ1uxXS9FOflgclGVigs8", 150),
    "pir": ("ПИР шашлык", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzNrSTKWuGogoS3i5mxUfKs9NIjibRxkMCsw&s", 100),
    "grizli": ("Гризли с крабом", "https://leader-dostavka.kz/upload/iblock/5cb/1o6lwdjph7o1k0svlma3ww62gljm9458.jpg", 95),

    "korm_1": ("Китекат", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYPvYOkfwfynNWBr0dPhpil5sx6R2U4m6vCA&s", 35),
    "korm_2": ("Вискас", "https://yac-wh-sb-prod-s3-media-07001.storage.yandexcloud.net/media/images/beef_350.max-2880x1820.format-png.png", 65),
    "korm_3": ("Феликс", "https://animal.kg/image/cache/catalog/felix/felix_simple_turkey-700x700.jpg", 40),
}


carts = {}


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
    await message.answer("📱 Добро пожаловать! В АЗИЮ:", reply_markup=kb.as_markup())


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


@router.callback_query(F.data.startswith("add:"))
async def add_item(callback: CallbackQuery):
    pid = callback.data.split(":")[1]
    user_id = callback.from_user.id
    carts.setdefault(user_id, []).append(pid)
    await callback.answer("✅ Товар добавлен в корзину!")


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


async def main():
    print("🤖 Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
