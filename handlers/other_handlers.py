from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from keyboards.inline_keyboard import create_inline_kb
from lexicon.lexicon import LEXICON_RU, GAMING_SITES_URLS
from services.news_parsing import get_list_news

# Инициализируем роутер уровня модуля
router = Router()


@router.message(F.text.lower() == '/info')
async def get_info(message: Message):
    keyboard = create_inline_kb(1, 'button_news_FG', 'button_news_FS')
    await message.answer(text='Источники:', reply_markup=keyboard)
    # await message.answer(get_list_news())


@router.callback_query(F.data == 'button_news_FG')
async def process_but_1_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=get_list_news(GAMING_SITES_URLS['Frictional_Games_url']),
        reply_markup=callback.message.reply_markup
    )


@router.callback_query(F.data == 'button_news_FS')
async def process_but_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=get_list_news(GAMING_SITES_URLS['Firefly_Studios_url']),
        reply_markup=callback.message.reply_markup
    )
