"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import datetime
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
def calculate_longest_call(calls):
    longest_call_phonenumber = None
    longest_call_duration= 0
    checked_phonenumbers= dict()
    emitter_phonenumber = None
    receiver_phonenumber = None
    emitter_duration = 0
    receiver_duration = 0
    for call in calls:
        emitter_phonenumber =  str(call[0])
        receiver_phonenumber = str(call[1])
        emitter_duration = checked_phonenumbers.get(emitter_phonenumber)
        if (emitter_duration is not None):
            checked_phonenumbers[emitter_phonenumber] = int(emitter_duration) + int(call[3])
            if (longest_call_duration < checked_phonenumbers[emitter_phonenumber]):
                longest_call_duration = checked_phonenumbers[emitter_phonenumber]
                longest_call_phonenumber = emitter_phonenumber
        else:
            checked_phonenumbers[emitter_phonenumber] = call[3]

        receiver_duration = checked_phonenumbers.get(receiver_phonenumber)
        if (receiver_duration is not None):
            checked_phonenumbers[receiver_phonenumber] = int(receiver_duration) + int(call[3])
            if (longest_call_duration < checked_phonenumbers[receiver_phonenumber]):
                longest_call_duration = checked_phonenumbers[receiver_phonenumber]
                longest_call_phonenumber = receiver_phonenumber
        else:
            checked_phonenumbers[receiver_phonenumber] = call[3] 
    return longest_call_phonenumber, longest_call_duration

result = calculate_longest_call(calls)
message = "{} spent the longest time, {} seconds, on the phone during September 2016."
print(message.format(result[0],result[1]))

    

            





         


#print(result)


