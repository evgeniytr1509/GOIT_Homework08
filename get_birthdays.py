import datetime

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