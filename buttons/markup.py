from typing import List

from aiogram.types import ReplyKeyboardMarkup

from buttons.user_text_markup import *
from buttons.admin_mentor_text_markup import *
from db import User


#
# def my_board_button(chat_id: str = None):
#     user: str = User(chat_id=chat_id).registered_user_chat_id()
#     row: List = [KeyboardButton(get_language('my_group', user[2])), KeyboardButton(get_language('new_group', user[2]))]
#     # row3: List = [get_language('rating', user[2])]
#     if not user[7].__eq__('STUDENT'):
#         row2: List = [KeyboardButton(get_language('my_cabinet', user[2]))]
#         return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[row2])
#     return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[row])

#
# def my_group_task_rating(lang_name):
#     row: List = [KeyboardButton(get_language('rating', lang_name)),
#                  KeyboardButton(get_language('group_task', lang_name))]
#     row2: List = [KeyboardButton(get_language('back_markup', lang_name))]
#     return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[row, row2])


# def _exit(lang_name):
#     row: List = [KeyboardButton(text=get_language('exit', lang_name))]
#     return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[row, ])


# PHONE_NUMBER_BUTTON = KeyboardButton(text='Phone Number', request_contact=True)
# def back():
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     back_key = KeyboardButton(text='back')
#     keyboard.add(back_key)
#     return keyboard


def phone_number():
	row: List = [KeyboardButton(text=PHONE_NUMBER_BUTTON_TEXT, request_contact=True)]
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[row, ])


def location():
	row: List = [KeyboardButton(text=LOCATION_BUTTON_TEXT, request_location=True)]
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[row, ], one_time_keyboard=True)


#
# def mentor_menu():
#     row1: List = [GROUPS_BUTTON, STUDENTS_BUTTON]
#     row2: List = [QUIZ_BUTTON, CREATE_GROUP_BUTTON]
#     row3: List = [ACTIVATE_STUDENT_BUTTON, ASSIGN_QUIZ_TO_GROUP_BUTTON]
#     row5: List = [SETTINGS_BUTTON, ]
#     keyboard: List = [row1, row2, row3, row5]
#     return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)
#
#
# def my_group():
#     row4: List = [CREATE_TASK, DELETE_TASK]
#     # row1: List = [GROUP_INFO]
#     keyboard: List = [row4]
#     return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)
#
#
# def admin_menu():
#     row1: List = [GROUPS_BUTTON, STUDENTS_BUTTON]
#     row2: List = [QUIZ_BUTTON, CREATE_GROUP_BUTTON]
#     row3: List = [ACTIVATE_STUDENT_BUTTON, SETTINGS_BUTTON]
#     keyboard: List = [row1, row2, row3]
#     return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)

CUSTOMER_BUTTON = '👗 Kelish Vaqti'
ARCHIVE = '📓 Arxiv'
ADMIN = '🅰️ Admin'
NEW_PRODUCT = '🆕 Yangi Maxsulotlar Qo\'shish'
CUSTOMER_LIST = '👯 Klientlar'
MY_PRODUCT = '📩 Maxsulotni Omborga Joylash'
SEAR = '🔎 Qidirish'
BACK = '⏮ Orqaga'
SEARCH = '🧑‍💻 Codesiz Clientlar'
REFRESH = '🔄 Refresh'


def my_board_button(chat_id: str):
	user = User(chat_id).admin_chat_id()
	row1: List = [CUSTOMER_BUTTON]
	row2: List = [NEW_PRODUCT, MY_PRODUCT]
	row3: List = [CUSTOMER_LIST, ARCHIVE]
	row4: List = [SEAR, ADMIN]
	keyboard: List = [row1]
	keyboard2: List = [row2, row3, row4]
	if not user:
		return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard2)


CREATE = '🔸 Admin Qo\'shish'
DELETE = '🗑 Admin O\'chirish'


def admin_create_delete_button():
	row1: List = [CREATE, DELETE]
	row2: List = [BACK]
	keyboard: List = [row1, row2]
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def back():
	row: List = [BACK, SEARCH]
	keyboard = [row]
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


YES = '🆗 Ha'


def yes():
	row: List = [BACK, YES]
	keyboard = [row]
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


def backs():
	row: List = [BACK]
	keyboard = [row]
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


ADD_ARCHIVE = '☑ Arxivdan olish'
DELETE_ARCHIVE = '❌ Arxivga olish'


def archive_button():
	row1: List = [ADD_ARCHIVE, DELETE_ARCHIVE]
	row2: List = [BACK]
	keyboard = [row1, row2]
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)


ALL_PRODUCT = '↙ Hamma Maxsulotlar'
ID_SEARCH = '🆔 ID bo\'yicha'
NAME_SEARCH = '📛 Ism bo\'yicha'
PHONE_NUMBER = '📱 Telefon'


def search_button():
	row1: List = [ID_SEARCH, NAME_SEARCH, PHONE_NUMBER]
	row2: List = [ALL_PRODUCT, BACK]
	keyboard = [row1, row2]
	return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)
