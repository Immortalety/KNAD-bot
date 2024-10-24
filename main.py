import ast
import asyncio
import operator
import random
import re
import requests

from enum import Enum
from time import time
from telebot.async_telebot import AsyncTeleBot
from telebot.types import *
from cat_names import cat_names


bot = AsyncTeleBot("*CENSORED*")

state = {}
state_message_id = {}


class State(Enum):
    NONE = 0
    SENT_IMAGE = 1
    WAIT_EXPRESSION = 2
    WAIT_TEXT = 3


operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.LShift: operator.lshift,
    ast.RShift : operator.rshift,
    ast.BitOr : operator.or_,
    ast.BitXor : operator.xor,
    ast.BitAnd : operator.and_,
    ast.FloorDiv: operator.floordiv,
    ast.Invert: operator.invert,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg
}

def evaluate(node) -> int:
    match node:
        case ast.Constant(value) if isinstance(value, int):
            return value
        case ast.BinOp(left, op, right):
            return operators[type(op)](evaluate(left), evaluate(right))
        case ast.UnaryOp(op, operand):
            return operators[type(op)](evaluate(operand))
        case _:
            raise TypeError(node)


def calculate(expression: str) -> int:
    return evaluate(ast.parse(expression, mode="eval").body)


def cat_count(n: int) -> str:
    if n >= 10 and n <= 14:
        return f"{n} котов"
    elif n % 10 == 1:
        return f"{n} кот"
    elif n % 10 >= 2 and n % 10 <= 4:
        return f"{n} кота"

    return f"{n} котов"


def menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🖼️ Картинка кота", callback_data="cat-picture"), InlineKeyboardButton("🔢 Калькулятор котов", callback_data="cat-calculator"))
    markup.add(InlineKeyboardButton("💡 Факт о котах", callback_data="cat-fact"), InlineKeyboardButton("📖 Коты в тексте", callback_data="cat-text"))
    markup.add(InlineKeyboardButton("🏷️ Имя для кота", callback_data="cat-name"))

    return markup


def back_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🐈 Вернуться назад", callback_data="cat-home"))

    return markup


@bot.message_handler(["start"])
async def message_handler(message: Message):
    state[message.chat.id] = State.NONE

    await bot.send_message(message.chat.id, "😺 Приветствую, здесь ты можешь найти множество функций, связанных с котами!", reply_markup=menu())


@bot.callback_query_handler(lambda query: query.data == "cat-home")
async def cat_home_handler(query: CallbackQuery):
    if state[query.message.chat.id] == State.SENT_IMAGE:
        await bot.delete_message(query.message.chat.id, state_message_id[query.message.chat.id])

    state[query.message.chat.id] = State.NONE

    await bot.edit_message_text("😺 Выбери, что ты хочешь сделать:", query.message.chat.id, query.message.message_id, reply_markup=menu())


@bot.callback_query_handler(lambda query: query.data == "cat-picture")
async def cat_picture_handler(query: CallbackQuery):
    state[query.message.chat.id] = State.SENT_IMAGE

    await bot.edit_message_text("😻 Отправляю картинку...", query.message.chat.id, query.message.message_id, reply_markup=back_menu())
    message = await bot.send_photo(query.message.chat.id, f"https://cataas.com/cat?time={int(time())}") # Добавляем time, чтобы Telegram не кешировал фото

    state_message_id[query.message.chat.id] = message.message_id


@bot.callback_query_handler(lambda query: query.data == "cat-calculator")
async def cat_calculator_handler(query: CallbackQuery):
    state[query.message.chat.id] = State.WAIT_EXPRESSION
    state_message_id[query.message.chat.id] = query.message.message_id

    await bot.edit_message_text("😼 Отправьте математическое выражение для подсчёта котов", query.message.chat.id, query.message.message_id, reply_markup=back_menu())


@bot.message_handler(func=lambda message: state[message.chat.id] == State.WAIT_EXPRESSION)
async def cat_calculator_result_handler(message: Message):
    state[message.chat.id] = State.NONE

    try:
        result = calculate(message.text)
    except Exception:
        text = "😾 Столько котов не бывает!"
    else:
        result_text = cat_count(result)

        if result < 0:
            text = "😾 Столько котов не бывает!"
        elif result == 0:
            text = "😿 Ни одного кота..."
        elif result == 1:
            text = f"😼 {result_text}, который гулял сам по себе"
        elif result < 10:
            text = f"😺 {result_text}"
        elif result < 100:
            text = f"😻 {result_text}, это много!"
        else:
            text = f"🙀 {result_text}, ЭТО ЗАМЕЧАТЕЛЬНО!!!"

    await bot.delete_message(message.chat.id, message.message_id)
    await bot.edit_message_text(text, message.chat.id, state_message_id[message.chat.id], reply_markup=back_menu())


@bot.callback_query_handler(lambda query: query.data == "cat-fact")
async def cat_fact_handler(query: CallbackQuery):
    request = requests.get("https://catfact.ninja/fact")

    if request.status_code == 200:
        fact = request.json()["fact"]
    else:
        fact = "😸 Не могу отправить интересный факт, но коты все равно классные!"

    await bot.edit_message_text(f"🙀 {fact}", query.message.chat.id, query.message.message_id, reply_markup=back_menu())


@bot.callback_query_handler(lambda query: query.data == "cat-text")
async def cat_text_handler(query: CallbackQuery):
    state[query.message.chat.id] = State.WAIT_TEXT
    state_message_id[query.message.chat.id] = query.message.message_id

    await bot.edit_message_text("😼 Отправьте текст и я скажу, сколько раз в нём упоминаются коты", query.message.chat.id, query.message.message_id, reply_markup=back_menu())


@bot.message_handler(func=lambda message: state[message.chat.id] == State.WAIT_TEXT)
async def cat_text_result_handler(message: Message):
    state[message.chat.id] = State.NONE

    cat_matches = re.findall(r"\bко[тш]\w*", message.text, re.IGNORECASE)
    cat_matches_count = len(cat_matches)

    if cat_matches_count == 0:
        text = "😿 Коты не упоминаются ни разу..."
    else:
        text = f"😺 В тексте {cat_count(cat_matches_count)}"

    await bot.delete_message(message.chat.id, message.message_id)
    await bot.edit_message_text(text, message.chat.id, state_message_id[message.chat.id], reply_markup=back_menu())


@bot.message_handler(func=lambda message: state[message.chat.id] == State.WAIT_TEXT)
async def cat_text_result_handler(message: Message):
    state[message.chat.id] = State.NONE

    cat_matches = re.findall(r"\bко[тш]\w*", message.text, re.IGNORECASE)
    cat_matches_count = len(cat_matches)

    if cat_matches_count == 0:
        text = "😿 Котов в тексте нет..."
    else:
        text = f"😺 В тексте {cat_count(cat_matches_count)}"

    await bot.delete_message(message.chat.id, message.message_id)
    await bot.edit_message_text(text, message.chat.id, state_message_id[message.chat.id], reply_markup=back_menu())


@bot.callback_query_handler(lambda query: query.data == "cat-name")
async def cat_name_handler(query: CallbackQuery):
    cat_emoji = random.choice(['😺', '😸', '😻', '😼'])
    cat_name_comment = random.choice(["Великолепное", "Запоминающееся", "Идеальное", "Классное", "Крутое", "Отличное", "Прекрасное", "Хорошее"])
    cat_name = random.choice(cat_names)

    await bot.edit_message_text(f"{cat_emoji} {cat_name_comment} имя для вашего кота — {cat_name}", query.message.chat.id, query.message.message_id, reply_markup=back_menu())


def main():
    logger.setLevel(logging.INFO)
    asyncio.run(bot.polling())


if __name__ =="__main__":
    main()