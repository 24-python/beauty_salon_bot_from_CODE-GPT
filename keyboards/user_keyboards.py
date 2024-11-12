from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_service_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Записаться'))
    keyboard.add(KeyboardButton('Отзывы'))
    return keyboard
