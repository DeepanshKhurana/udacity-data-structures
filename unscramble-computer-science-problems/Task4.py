"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = []
receivers = []

for caller, receiver, date, time in calls:
    callers.append(caller)
    receivers.append(receiver)
    
potential_callers = [number for number in callers if number not in receivers]

senders = []
recipients = []

for sender, recipient, date in texts:
    senders.append(sender)
    recipients.append(recipient)
    
texting_numbers = set(senders + recipients)
telemarketers = [number for number in potential_callers if number not in texting_numbers]

telemarketers.sort()

print('These numbers could be telemarketers:')
for number in set(telemarketers):
    print(number)