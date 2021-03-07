import time
import psutil
from win10toast import ToastNotifier #For notification

def shownotification():
    toaster = ToastNotifier()
    toaster.show_toast("Battery Alert" , "Battery charged to 100%. Remove charger",duration=5,
                       icon_path="PATH_TO_ICON")
charged = False

while 1:
    battery = psutil.sensors_battery() #Initialization
    plugged = battery.power_plugged #Checks whether the charger is plugged or not
    percent = battery.percent #Gets the percentage of the battery
    removed = False 
    if plugged:
        if percent == 100:
            shownotification() #Shows notification if Plugged and the Percentage is 100
            time.sleep(60) #Repeatedly pops up the notification if the charger is not unplugged
            charged = True 
            continue
    if charged: 
        time.sleep(60*30) #To reduce the CPU Usage
    else:
        time.sleep(60*5) #To repeatedly keep checking the percentage every 5 Minute cycle
