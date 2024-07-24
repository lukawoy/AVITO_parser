from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from keyboards.inline_keyboard import create_inline_kb
from lexicon.lexicon import LEXICON_RU
from services.get_news_FG import get_list_news

# Инициализируем роутер уровня модуля
router = Router()


@router.message(F.text.lower() == '/info')
async def get_info(message: Message):
    keyboard = create_inline_kb(1, 'button_get_news')
    await message.answer(text='Источники:', reply_markup=keyboard)
    # await message.answer(get_list_news())


@router.callback_query(F.data == 'button_get_news')
async def process_but_1_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=get_list_news(),
        reply_markup=callback.message.reply_markup
    )
