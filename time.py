print ("Welcome To Time Version 1.0") 

from datetime import datetime

def get_12_hour_time():
    now = datetime.now()
    return now.strftime("%I:%M:%S %p")

print("Current time:", get_12_hour_time())
