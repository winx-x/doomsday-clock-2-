###     IMPORTING:  ###

from appJar import gui
import sys
from datetime import datetime, time
from time import sleep
import os
import Links as l
from PIL import Image, ImageTk
import webbrowser



###    VARIABLES:  ###

doomsday=0
    # yup, I made it global, it was the only option

###    FUNCTIONS:  ###

def pick(number):
    # for picking video link and quote
    return l.movies[number]

def launch(win):
    #launchs subwindow
    DoomsdayClock.showSubWindow(win)

def close():
    # closes subwindow
    DoomsdayClock.hideSubWindow("Pick THE DAY")

def exit():
    # stops program
    DoomsdayClock.stop()

def play():
    # for button 'play' ==> opens youtube
    DoomsdayClock.stopSound()
    new=2
    td = days_between_dates()
    linker=pick(td.days)
    webbrowser.open(linker.link, new=new)
    
def press():
    # for link '-1' ==> opens youtube
    DoomsdayClock.stopSound()
    new=2
    td = days_between_dates()
    linker='https://www.youtube.com/watch?v=wEWF2xh5E8s'
    webbrowser.open(linker, new=new)

def start():
        # program's heart (ok, core)
        #Changing labels
    DoomsdayClock.setLabel('lbl1', 'Today is: ')
    DoomsdayClock.setLabel('lbl2', datetime.now())
    #DoomsdayClock.setLabel('lbl3', 'Let\'s pick The Day ')
        #removing button
    DoomsdayClock.removeButton('Start!')
        # addding button
    DoomsdayClock.addButton("Pick THE DAY", launch)
    datePicking()

def datePicking():
    # adding datepicker
    DoomsdayClock.startSubWindow("Pick THE DAY", modal=True)
    DoomsdayClock.setLocation(x=1, y=1)
    DoomsdayClock.setBg('black')
    DoomsdayClock.setFg('red')
    DoomsdayClock.addLabel("l1", "Let\'s pick The Day")
    DoomsdayClock.addDatePicker('The Day')
    DoomsdayClock.setDatePickerRange('The Day', 2019, 2100)
    DoomsdayClock.setDatePicker('The Day')
    DoomsdayClock.addButton('GET', showDate)
    DoomsdayClock.stopSubWindow()

def showDate():
        # showing 'the end' date and moving to countdown
    DoomsdayClock.removeButton('Pick THE DAY')
    DoomsdayClock.addLabel('lbl4', 'Doomday is: ')
    DoomsdayClock.addLabel('lbl5', DoomsdayClock.getDatePicker('The Day'))
    global doomsday
    doomsday1=DoomsdayClock.getDatePicker('The Day')
    close()
    day=doomsday1.day
    month=doomsday1.month
    year=doomsday1.year
    doomsday=datetime(year, month, day)
    countdown()

def countdown():
    # countdown function, not perfect, but working
    global doomsday
    now=datetime.now()
    DoomsdayClock.addMessage("mess", '')
        # This is one, big 'mess'
    if doomsday>now:
        DoomsdayClock.setFg('red')
        td = days_between_dates()
        days, hours, minutes, seconds = td.days, td.seconds // 3600, td.seconds // 60 % 60, td.seconds%60
        DoomsdayClock.setMessage("mess", ("Remains:", days, "days", hours, "hours",minutes, "minuts", seconds, "seconds."))
        if td.days<=30:
            linker=pick(td.days)
            DoomsdayClock.addLabel('lbl6', 'Today\'s quote:')
            DoomsdayClock.setLabelFg('lbl6', 'orange')
            DoomsdayClock.addLabel('lbl7', linker.quote)
            DoomsdayClock.setLabelFg('lbl7', 'orange')
            DoomsdayClock.addButton('Play dedicated video', play)
    else:
        DoomsdayClock.addLabel('lbl6', 'It\'s all over now')
        DoomsdayClock.addButton('Play dedicated video', press)
        DoomsdayClock.setLabelFg('lbl6', 'orange')
    DoomsdayClock.addButton('Exit', exit)

def days_between_dates():
    #różnica w datach
    now=datetime.now()
    global doomsday
    difference=doomsday-now
    return difference
    #jeżeli mają być same dni, to difference.days


###    MAIN CODE:  ###

#creating gui
DoomsdayClock=gui('Apocalypse!', showIcon=False)
#DoomsdayClock.setIcon('Pics\Boom.jpg')
DoomsdayClock.setSize('Fullscreen')
DoomsdayClock.setResizable(True)
DoomsdayClock.setBg('black')
DoomsdayClock.setFg('brown')
DoomsdayClock.setFont(20)

DoomsdayClock.showSplash('End is near, reality is an illusion', fill='red', stripe='black', fg='white', font=44)
    # For welcome screen

DoomsdayClock.playSound('Music\Funeral_march.wav', wait=False)
    # Everybody loves good music ^^

DoomsdayClock.addLabel('lbl1', 'Wanna start?')
#DoomsdayClock.image('End is near, reality is an illusion', value='The_end.gif') <== hell no, program is crashing like hell

DoomsdayClock.addLabel('lbl2', 'Course u do!')
DoomsdayClock.addButton('Start!', start)

DoomsdayClock.go()
    #running gui, !it has to be at the very end of code!
