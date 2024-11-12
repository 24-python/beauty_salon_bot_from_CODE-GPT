import sqlite3

DB_PATH = 'beauty_salon.db'

# Функция инициализации базы данных (создаёт таблицы, если их нет)
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Создание таблицы мастеров
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS masters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            service TEXT,
            schedule TEXT  -- Время работы мастера, например, "Пн-Пт: 10-18"
        )
    ''')
    
    # Создание таблицы услуг
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration INTEGER -- Продолжительность услуги в минутах
        )
    ''')
    
    # Создание таблицы записей клиентов
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

# Функция для выполнения SQL-запросов
def execute_query(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Функция для получения данных из базы
def fetch_query(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results
