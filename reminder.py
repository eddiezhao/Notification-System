from plyer import notification
import time


ttl = ""
msg = ""

def setReminder(title, message):
   ttl = title
   msg = message
   notification.notify(title = ttl,
                       message = msg,
                       app_name = "Reminder",
                       app_icon = None,
                       timeout = 10,
                       ticker = "oop")

