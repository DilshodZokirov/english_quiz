from aiogram import typesfrom aiogram.dispatcher import FSMContextfrom aiogram.types import ReplyKeyboardRemovefrom buttons.inlines import language_buttonfrom buttons.markup import phone_number, my_board_buttonfrom buttons.user_text_markup import REGISTER_BUTTON, PHONE_NUMBER_BUTTON_TEXTfrom db.mappers import dict_to_userfrom dispatch import dpfrom states import ForceToRegister, RegisterState, BeginState@dp.message_handler(lambda message: str(message.text).__eq__(REGISTER_BUTTON), state=ForceToRegister.begin_register)async def user_register_handler(message: types.Message, state: FSMContext):	async with state.proxy() as data:		pass	text = 'Iltimos tilni tanlang'	text2 = 'Marxamat'	await RegisterState.language.set()	await message.bot.send_message(chat_id=message.chat.id, text=text, reply_markup=language_button())	await message.bot.send_message(chat_id=message.chat.id, text=text2, reply_markup=ReplyKeyboardRemove())@dp.callback_query_handler(state=RegisterState.language)async def language_handler(query: types.CallbackQuery, state: FSMContext):	async with state.proxy() as data:		data['lang'] = query.data	await query.message.delete()	text = 'Iltimos ismizni kiriting'	await RegisterState.next()	await query.message.bot.send_message(text=text, chat_id=query.message.chat.id)@dp.message_handler(state=RegisterState.name)async def create_name_handler(message: types.Message, state: FSMContext):	async with state.proxy() as data:		data['name'] = message.text	text = 'Iltimos yoshingizni kiriting'	await RegisterState.next()	await message.reply(text=text)@dp.message_handler(state=RegisterState.age)async def age_state_handler(message: types.Message, state: FSMContext):	age: str = message.text	if not age.isdigit():		await message.delete()		return	async with state.proxy() as data:		data['age'] = message.text	text = 'Telefon nomerni kiriting'	await RegisterState.next()	await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=phone_number())@dp.message_handler(content_types=types.ContentType.CONTACT,                    state=RegisterState.phone_number)async def phone_number_handler(message: types.Message, state: FSMContext):	async with state.proxy() as data:		data['phone_number'] = dict(message.contact)		data['chat_id'] = message.chat.id	user = dict_to_user(data)	user.insert_into_user()	text = 'Muaffaqiyatli amalga oshdi'	await BeginState.begin.set()	await message.bot.send_message(text=text, chat_id=message.chat.id, reply_markup=my_board_button(message.chat.id))