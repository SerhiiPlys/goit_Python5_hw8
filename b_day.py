"""К сдаче ДЗ 8
   
"""
from datetime import datetime

d_test = ([ {"name":"Vlad","birthday":"1988-02-05"},
            {"name":"Mike","birthday":"1982-02-09"},
            {"name":"Uncle Ben","birthday":"1969-02-12"},
            {"name":"Polly","birthday":"1990-08-30"} ])

def nts_weekday(cnt):
    number = cnt%7
    if number == 0:
        day = "Monday"
    elif number == 1:
        day = "Tuesday"
    elif number == 2:
        day = "Wednesday"
    elif number == 3:
        day = "Thirsday"
    elif number == 4:
        day = "Friday"
    elif number == 5:
        day = "Saturday"
    else:
        day = "Sunday"
    return day

def get_birthdays_per_week(d_in):
    for i in d_in:
        t_now = datetime.now() # получаем текущий дату
        year_now = t_now.year  # конкретно год
        s1 = i["birthday"]
    #    print(s1)  # оригинальный дата рождения
        l1 = s1.split('-')
        l1[0] = str(year_now) 
        s2 = '-'.join(l1)     # эти 4 строки подменят год рождения на текущий
        t1 = datetime.strptime(s2, '%Y-%m-%d') # получаем обьект дата с числами рождения но текущим годом
    #    print(t1) # приведенный год рождения
        t_dif = t1 - t_now # разница в днях от дня рождения ожидаемого до сегодня
    #    print(t_dif.days) # особенность при одинаковых числах разница дней = -1, завтра будет 0 разница
        # следующая строка-условие говорит что если сегодня (когда запустили скрипт) понедельник
        # и были дни рождения вчера и позавчера, то поздравить сегодня в этот понедельник!
        if (t_now.weekday() == 0) and ((t_dif.days == -2) or (t_dif.days == -3)):
            print("On This Monday: - should Congr to  " + i["name"] + "  his BD was on weekend")
        # следующее условие - возможные именники в предстоящую неделю
        if (t_dif.days <= 7) and (t_dif.days >= 0):
            brs_wkd = t_now.weekday() + t_dif.days + 1 # день недели когда будет ДР
            if brs_wkd == 5:  # ДР в ближайшую субботу - поздравить в Пн 
                print("On next Monday: - should Congr to  " + i["name"] + "  his BD will be on Saturday")    
            elif brs_wkd == 6: # ДР в ближайшее воскресенье - поздравить в Пн
                print("On next Monday: - should Congr to  " + i["name"] + "  his BD will be on Sunday")  
            else:
                print(nts_weekday(brs_wkd) +\
                      ": - should Congr to  "+ i["name"])

if __name__ == "__main__":
    get_birthdays_per_week(d_test)
