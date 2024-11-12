import os

# Telegram Bot Token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Список ID администраторов
ADMIN_IDS = [123456789, 987654321]

# Путь к базе данных
DB_PATH = 'beauty_salon.db'

# Уведомления (за сколько времени до записи напомнить клиенту)
REMINDER_TIME_MINUTES = 60
