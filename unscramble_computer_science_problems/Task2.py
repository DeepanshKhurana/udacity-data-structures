from collections import Counter
from datetime import datetime

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

receivers = Counter({})
callers = Counter({})

for caller, receiver, date, time in calls:
    # No need to check for dates since all of our data is from September 2016
    callers[receiver] += int(time)
    receivers[receiver] += int(time)

phone_calls = receivers + callers

highest_time_key = max(phone_calls, key=phone_calls.get)
    
print(f'{highest_time_key} spent the longest time, {phone_calls[highest_time_key]} seconds, on the phone during September 2016.')


