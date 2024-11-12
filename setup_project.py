import os

# Структура проекта
project_structure = {
    "beauty_salon_bot": [
        "main.py",
        "config.py",
        "database.py",
        "handlers/__init__.py",
        "handlers/user_handlers.py",
        "handlers/admin_handlers.py",
        "keyboards/__init__.py",
        "keyboards/user_keyboards.py",
        "keyboards/admin_keyboards.py",
        "services/__init__.py",
        "services/booking.py",
        "services/masters.py",
        "services/notifications.py",
        "utils/__init__.py",
        "utils/validators.py",
        "utils/state_machine.py"
    ]
}

# Шаблоны для файлов
file_templates = {
    "main.py": '''from aiogram import Bot, Dispatcher, executor
from config import TOKEN
from database import init_db
from handlers import user_handlers, admin_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Инициализация базы данных
init_db()

# Регистрация обработчиков
user_handlers.register_handlers(dp)
admin_handlers.register_handlers(dp)

if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)
''',

    "config.py": '''import os

# Telegram Bot Token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Список ID администраторов
ADMIN_IDS = [123456789, 987654321]

# Путь к базе данных
DB_PATH = 'beauty_salon.db'

# Уведомления (за сколько времени до записи напомнить клиенту)
REMINDER_TIME_MINUTES = 60
''',

    "database.py": '''import sqlite3

DB_PATH = 'beauty_salon.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS masters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            service TEXT,
            schedule TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration INTEGER
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            master_id INTEGER,
            service_id INTEGER,
            booking_time TEXT,
            status TEXT DEFAULT 'pending',
            rating INTEGER DEFAULT NULL,
            feedback TEXT DEFAULT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
'''
}

# Создание папок и файлов
def create_project_structure(structure, templates):
    for root, files in structure.items():
        if not os.path.exists(root):
            os.makedirs(root)
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    # Заполняем файл шаблоном, если он есть
                    template_name = os.path.basename(file)
                    content = templates.get(template_name, '')
                    f.write(content)
                print(f"Создан файл: {file_path}")

# Инициализация проекта
create_project_structure(project_structure, file_templates)

print("\n✅ Все необходимые файлы и папки созданы. Проект готов к тестированию!")
