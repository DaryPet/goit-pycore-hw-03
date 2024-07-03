from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    print(today)

    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        print (birthday_date)
        birthday_this_year = birthday_date.replace(year=today.year)
        print(birthday_this_year)

        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(yea = today.year+1)

        

        

    return birthday_date




users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Ann Miki", "birthday": "1990.07.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
