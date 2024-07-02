
from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у об'єкт datetime
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        
        # Отримуємо поточну дату
        current_date = datetime.today().date()
        
        # Розраховуємо різницю у днях
        delta = current_date - date_obj
        
        # Повертаємо різницю у днях як ціле число
        return delta.days
    except ValueError:
        # Якщо виникає помилка (наприклад, неправильний формат дати), повертаємо None
        return None
