
from datetime import datetime, timedelta 

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()    
        birthday_this_year = birthday_date.replace(year=today.year)
       
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= 7:
            if birthday_this_year.weekday() == 5:  # Суббота
                congr_date = birthday_this_year + timedelta(days=2)  # перенос на понедельник
            elif birthday_this_year.weekday() == 6:  # Воскресенье
                congr_date = birthday_this_year + timedelta(days=1)  # перенос на понедельник
            else:
                congr_date = birthday_this_year  # Используем дату дня рождения, если не выходной

            upcoming_birthdays.append({
                "name": user["name"],
                "congrats_day": congr_date.strftime("%Y.%m.%d") 
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Ann Miki", "birthday": "1990.07.07"},
    {"name": "An Mi", "birthday": "1990.07.05"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
