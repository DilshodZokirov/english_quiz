from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup

import states
from buttons.markup import REGISTER_BUTTON, my_board_button
from configs.constants import LOGO, BOT_NAME
from dispatch import dp
from db import User
from states import BeginState


@dp.message_handler(commands="start", state='*')
async def start(message: types.Message, state: FSMContext):
	# if message.from_user.last_name:
	message_body = f"""
            Salom {message.from_user.last_name or message.from_user.first_name}\n xush kelibsiz bizning {BOT_NAME} botga!!!
    """
	user: User = User(chat_id=message.chat.id).registered_user_chat_id()
	if not user:
		markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
		button = REGISTER_BUTTON
		markup.add(button)
		await states.ForceToRegister.begin_register.set()
		await message.bot.send_photo(chat_id=message.chat.id, photo=open(LOGO, mode="rb"), caption=message_body)
		await message.bot.send_message(chat_id=message.chat.id,
		                               text="Register tugmasini bosing", reply_markup=markup)
		return
	async with state.proxy() as data:
		pass
	text = '''Siz registratsiyadan o\'tgansiz'''
	await BeginState.begin.set()
	await message.bot.send_message(text=text, chat_id=message.chat.id,
	                               reply_markup=my_board_button(message.chat.id))


@dp.message_handler(commands="help")
async def help(message: types.Message):
	message_body = "Here You Cann find Some Trashes"
	await message.reply(message_body)
