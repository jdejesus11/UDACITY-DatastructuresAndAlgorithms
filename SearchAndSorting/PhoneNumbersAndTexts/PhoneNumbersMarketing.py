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

def get_telemarketing_phonenumbers(calls,texts):
    telemarketing_phonenumbers = []
    texted_phonenumbers = []
    incoming_call_phonenumbers = []
    for call in calls:
        is_telemarketing = True
        if (call[0] not in texted_phonenumbers):
            for text in texts:
                if (call[0] == str(text[0]) or call[0] == str(text[1])):
                    is_telemarketing = False
                    texted_phonenumbers.append(call[0])
                    break
            if (is_telemarketing == True):
                if (call[1] not in incoming_call_phonenumbers):
                    incoming_call_phonenumbers.append(call[1])
                if (call[0] not in incoming_call_phonenumbers):
                    if (call[0] not in telemarketing_phonenumbers):
                        telemarketing_phonenumbers.append(call[0])
    return telemarketing_phonenumbers

result = get_telemarketing_phonenumbers(calls,texts)
print("These numbers could be telemarketers: ")
for number in result:
    print(number)


                
            


