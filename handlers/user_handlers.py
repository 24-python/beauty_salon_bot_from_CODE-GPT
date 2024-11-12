from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from services.booking import start_booking, confirm_booking
from keyboards.user_keyboards import get_service_menu

# Приветствие пользователя
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в наш салон красоты!", reply_markup=get_service_menu())

# Начало процесса бронирования
async def handle_booking(message: types.Message):
    await start_booking(message)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(handle_booking, Text(equals='Записаться'))
