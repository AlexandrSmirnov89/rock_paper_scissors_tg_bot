from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# с использованием билдера
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)


# без использования билдера
rock_button = KeyboardButton(text=LEXICON_RU['rock'])
paper_button = KeyboardButton(text=LEXICON_RU['paper'])
scissors_button = KeyboardButton(text=LEXICON_RU['scissors'])

game_kb = ReplyKeyboardMarkup(keyboard=[[rock_button, paper_button, scissors_button]],
                              resize_keyboard=True)