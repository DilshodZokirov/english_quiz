from aiogram.dispatcher.filters.state import StatesGroup, Stateclass ForceToRegister(StatesGroup):	begin_register = State()class BeginState(StatesGroup):	begin = State()class RegisterState(StatesGroup):	language = State()	name = State()	age = State()	phone_number = State()class MyGroup(StatesGroup):	begin = State()class NewGroup(StatesGroup):	begin = State()	finish = State()