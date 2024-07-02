from datetime import datetime


def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        print(date_obj)
        current_date = datetime.today().date()
        print(current_date)

        delta = current_date - date_obj
        return delta.days
    except ValueError:
        return "Error"

date_input = "2025-07-24"
days_difference = get_days_from_today(date_input)
print(days_difference)