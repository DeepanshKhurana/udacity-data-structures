"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A

bangalore_codes = []
pattern = re.compile('(\([0-9]+\))')

for caller, receiver, date, time in calls:
    matched = pattern.match(receiver)
    if caller.startswith('(080)'):
        if receiver.startswith('140'):
            bangalore_codes.append(receiver)
        elif receiver.startswith(('7', '8', '9')):
            bangalore_codes.append(receiver[0:4])
        elif matched:
            bangalore_codes.append(matched.group(1)) 
            
bangalore_codes.sort()

print('The numbers called by people in Bangalore have codes:')
for code in set(bangalore_codes):
    print(code)
    
# Part B

calls_to_bangalore = 0

for code in bangalore_codes:
    if code == '(080)':
        calls_to_bangalore += 1

result = round((calls_to_bangalore * 100 )/ len(bangalore_codes), 2)
        
print(f'{result} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
