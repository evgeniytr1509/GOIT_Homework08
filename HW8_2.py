from datetime import datetime, timedelta
import datetime

def get_birthdays_per_week(users): 
    
    now = datetime.now().date()# текущая дата
    current_weekday = now.weekday() # текущая дата
    week_start = now - timedelta(current_weekday) # начано недели
    week_end = week_start + timedelta(6) # конец недели
    
    print (f"текущая дата {now}")
    print(f"день недели {current_weekday}")
    print (f"начало недели {week_start}")
    print (f"конец недели {week_end}")

    print ("Geltenmen, this week is your birthday. My congratulations and best wishes.")
    for user in users:
        
        bday = user['birthday'].date() # дни рождения 
        
        if week_start.month == bday.month: # проверка на совпадение месяца
            if week_start.day <= bday.day <= week_end.day: # поиск дня рождения на текущей неделе
                print(f"{bday.strftime('%d.%m.%Y')} - {user['name']}")

users = [
    {'name': 'Akira Kurosava', 'birthday': datetime(1910, 3, 23)},
    {'name': 'Albert Einstein', 'birthday': datetime(1879, 3, 14)},
    {'name': 'Albert Alexandre Louis Pierre Prinse of Monaco', 'birthday': datetime(1958, 3, 14)},
    {'name': 'Amerigo Vespucci', 'birthday': datetime(1454, 3, 9)},
    {'name': 'Antonio Lucio Vivaldi', 'birthday': datetime(1678, 3, 4)},
    {'name': 'Alexander Graham Bell', 'birthday': datetime(1847, 3, 3)},
    {'name': 'Bruce Willis', 'birthday': datetime(1955, 3, 19)}
]
get_birthdays_per_week(users)


def get_birthdays(birthdays): 


    birthdays = {"Akira Kurosava": "1910, 3, 23", 
                "Albert Einstein": "1879, 3, 14", 
                "Albert Alexandre Louis Pierre Prinse of Monaco": "1958, 3, 14",
                "Amerigo Vespucci": "1454, 3, 9",
                "Antonio Lucio Vivaldi": "1678, 3, 4",
                "Alexander Graham Bell": "1847, 3, 3", 
                "Bruce Willis": "1955, 3, 19"}
    for name, birthday in birthdays.items():
        year, month, day = map(int, birthday.split(", "))
        weekday = datetime.date(2023, month, day).strftime("%A")
        print(f"{name}' birthday is on a {weekday}")

get_birthdays(get_birthdays)