from aiogram.types import KeyboardButtonfrom configs.emojis import PHONE, REGISTER, LOCATIONREGISTER_BUTTON_TEXT = f"{REGISTER} Register"REGISTER_BUTTON = KeyboardButton(text=REGISTER_BUTTON_TEXT)# PHONE_NUMBER_BUTTON_TEXT = get_language('phone_number_button', data['lang'])PHONE_NUMBER_BUTTON_TEXT = F'{PHONE} Telifon Nomer'LOCATION_BUTTON_TEXT = F'{LOCATION} Locatsiya'LOCATION_BUTTON = KeyboardButton(text=LOCATION_BUTTON_TEXT, request_location=True)