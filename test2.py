from datetime import timedelta, datetime
import time
 
now = datetime.now()
print(now)
time.sleep(3)
later = datetime.now()
print(later)
if later - now > timedelta(seconds=2):
    print("hello")