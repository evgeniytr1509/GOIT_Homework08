from datetime import datetime, timedelta
now = datetime.now().date()# текущая дата
current_weekday = now.weekday() # текущая дата
week_start = now - timedelta(current_weekday) # начано недели
week_end = week_start + timedelta(6) # конец недели
import datetime

def get_birthdays(birthdays): 
    
    birthdays = {"Akira": "1910, 3, 23", 
                "Albert": "1879, 3, 14", 
                "Louis": "1958, 3, 15",
                "Amerigo": "1454, 3, 9",
                "Antonio": "1678, 3, 14",
                "Alexander": "1847, 3, 13", 
                "Bruce": "1955, 3, 19",
                "Jonh": "2000, 3, 18",
                "Bill": "2021, 3, 12",
                "Alise": "1955, 3, 11"}
        
    print ("Happy Birthday on this week:")
    print ("    Happy Birthday on work days:")
    for name, birthday in birthdays.items():# поиск дня рождения на текущей неделе
        year, month, day = map(int, birthday.split(", "))
        weekday = datetime.date(2023, month, day).strftime("%A")
        date = datetime.date(2023, month, day)
        
        if week_start.day <= date.day <= week_end.day: 
            if date.weekday() < 5:
                print (f"       {weekday} - {date} - {name}")

    print ("Happy Birthday on last dayof:")
    
    for name, birthday in birthdays.items():# поиск дня рождения на прошедших выходных
        
        year, month, day = map(int, birthday.split(", "))
        weekday = datetime.date(2023, month, day).strftime("%A")
        date = datetime.date(2023, month, day)
                
        if week_start.day > date.day:     
            if date.weekday() == 5 or date.weekday() == 6:
                print (f"       {name} - {weekday} - {date}")
get_birthdays(get_birthdays)






