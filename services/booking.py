from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import execute_query, fetch_query

# Машина состояний для процесса записи
class BookingFSM(StatesGroup):
    choosing_service = State()
    choosing_master = State()
    choosing_time = State()

# Начало бронирования
async def start_booking(message: types.Message, state: FSMContext):
    services = fetch_query("SELECT name FROM services")
    service_list = [s[0] for s in services]
    
    # Предложить пользователю выбор услуги
    await BookingFSM.choosing_service.set()
    await message.answer(f"Выберите услугу: {', '.join(service_list)}")

# Подтверждение записи
async def confirm_booking(message: types.Message, state: FSMContext):
    booking_time = message.text
    data = await state.get_data()
    service_id = data.get('service_id')
    master_id = data.get('master_id')
    
    execute_query("INSERT INTO bookings (user_id, master_id, service_id, booking_time) VALUES (?, ?, ?, ?)",
                  (message.from_user.id, master_id, service_id, booking_time))
    await message.answer("Запись успешно создана!")
    await state.finish()
