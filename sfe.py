from datetime import datetime
from turtle import *

class Alarm:
    def __init__(self):
        self.alarm = ["",""]
        self.tl = Turtle()
        
    def currentTime(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print("Current time = ",time)

    def get(self):
        a = int(input("Do you want alarm 1 or 2? "))
        if a> 2:
            exit
        if a == 1:
            a = 0
        else:
            a =1
        print("alarm ", a+1," is set at ",self.alarm[a]) 

    def setAlarm(self):
        time = input(str("Enter the time in 24 hour format 'H:M:S' "))
        if (self.alarm[0] is  ""):
            self.alarm[0] = time
            split_time = self.alarm[0].split(":")
            if (int(split_time[0]) > 24):
                print("Invalid Time")
                exit
            print("alarm one set")
            
        elif(self.alarm[1] is ""):
            self.alarm[1] = input(str("Enter the time in 24 hour format 'H:M:S'"))
            split_time = self.alarm[1].split(":")
            if (split_time[0] > 24):
                print("Invalid Time")
                exit
        
        else:
            print("Alarm is full. Please Delete One")

    def startAlarm(self):
        a = int(input("Do you want to start alarm 1 or 2 ? "))
        
        if a> 2:
            exit
        if a == 1:
            a = 0
        else:
            a =1
        self.tl.clear()
        self.tl.write(self.alarm[a])
        print("Alarm started")
        
if __name__ == "__main__":
    print(" Enter \n 'time' to view time \n 'setalarm' to set alarm \n 'getAlarm' to get alarm and 'start' to start alarm")
    Alarm = Alarm()
    time = Alarm.currentTime()
    setalarm = Alarm.setAlarm() 
    getAlarm = Alarm.get()
    start = Alarm.startAlarm()
