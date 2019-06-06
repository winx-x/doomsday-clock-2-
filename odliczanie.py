#odliczanie od dzisiaj do daty
from datetime import datetime, time
from time import sleep
import os
import sys

    #różnica w datach
def days_between_dates(today, the_end):
    difference=the_end-today
    return difference
    #jeżeli mają być same dni, to difference.days
now=datetime.now()
doomsday=datetime(2019,6,20)
td = days_between_dates(now, doomsday)
days, hours, minutes, seconds = td.days, td.seconds // 3600, td.seconds // 60 % 60, td.seconds%60


#odliczanie
while doomsday>now:
    print("pozostało:", days, "dni", hours, "godzin",minutes, "minut", seconds, "sekund")
    sleep(1)
    os.system('cls')
    now=datetime.now()
    td = days_between_dates(now, doomsday)
    days, hours, minutes, seconds = td.days, td.seconds // 3600, td.seconds // 60 % 60, td.seconds%60
