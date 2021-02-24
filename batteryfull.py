import time
import psutil
from win10toast import ToastNotifier
import time


def shownotification():
    toaster = ToastNotifier()
    toaster.show_toast("Battery Alert", "Battery charged to 100%. Remove charger",duration=5,
                       icon_path="PATH_TO_ICON")
charged = False

while 1:
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    removed = False
    if plugged: #CHECKS IF THE CHARGER IS PLUGGED IN OR NOT
        if percent == 100:
            shownotification() #SHOWS A NOTIFICATION FOR 5 SECONDS
            time.sleep(60) #REPEATEDLY SHOWS UNTIL UNPLUGGES
            charged = True 
            continue
    if charged:
        time.sleep(60*30) #SLEEPS FOR 30 MINUTES SUCH THAT THE LOOP IS NOT RUNNING. SAVES CPU UTILIZATION
    else:
        time.sleep(60*5)
