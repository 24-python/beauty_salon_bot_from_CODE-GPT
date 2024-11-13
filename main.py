from aiogram import Bot, Dispatcher, executor
from config import TOKEN
from database import init_db
from handlers import user_handlers, admin_handlers


# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Инициализация базы данных
init_db()

# Регистрация всех хендлеров
user_handlers.register_handlers(dp)
admin_handlers.register_handlers(dp)

# Запуск бота
if __name__ == "__main__":
    print("Бот успешно запущен!")
    executor.start_polling(dp, skip_updates=True)
