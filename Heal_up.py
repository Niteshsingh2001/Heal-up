import time
from notifypy import Notify

interval = int(input("Enter Interval time in mins : "))
break_timr = int(input("Enter break time in mins : "))

t2= time.localtime().tm_min + interval

while True:
	t1= time.localtime().tm_min 	
	if t1 ==t2:

		notification = Notify()
		notification.application_name = "Heal up"
		notification.title = "Heal yourself"
		notification.message = "Drink Water\nRelax Eyes\nStretch Body"
		notification.icon = "Simple-Ways-To-Balance-Your-Chakras-1024x1024.jpg"
		notification.audio = "mixkit-uplifting-flute-notification-2317.wav"
		notification.send()
		
		time.sleep(break_timr*60)
		notification.icon = "remote.jpg"		
		notification.title = "Back to work"
		notification.message = "Let's do it"
		notification.audio = "mixkit-game-success-alert-2039.wav"
		notification.send()
		t2= time.localtime().tm_min + interval
	continue
