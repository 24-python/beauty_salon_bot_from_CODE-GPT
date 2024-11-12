import asyncio
from aiogram import Bot
from config import TOKEN, REMINDER_TIME_MINUTES
from database import fetch_query

bot = Bot(token=TOKEN)

async def send_reminder():
    bookings = fetch_query("SELECT user_id, booking_time FROM bookings WHERE status='pending'")
    for user_id, booking_time in bookings:
        # Проверка времени и отправка напоминания (пример)
        await bot.send_message(user_id, "Напоминаем, у вас запись через 1 час!")
