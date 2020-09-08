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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def IsNumberRepeated(repeated_numbers, number):
    index = 0
    isRepeated = False
    while (index < len(repeated_numbers)):
        if (repeated_numbers[index] == number):
            isRepeated = True
            break
        index+=1

    return isRepeated

def DeleteNumber(phone_numbers, number):
    index = 0
    result = []
    for value in phone_numbers:
        if (value != number):
            result.append(value)
    return result

def CalculateDifferentTelephoneNumbers(data,no_repeated_numbers_accum):
    repeated_numbers = []
    no_repeated_numbers = no_repeated_numbers_accum
    for value in data:
        if (IsNumberRepeated(repeated_numbers,value[0]) == False):
            repeated_numbers.append(value[0])
            no_repeated_numbers.append(value[0])
        else:
            no_repeated_numbers = DeleteNumber(no_repeated_numbers,value[0])   
        if (IsNumberRepeated(repeated_numbers,value[1]) == False):
            repeated_numbers.append(value[1])
            no_repeated_numbers.append(value[1])
        else:
            no_repeated_numbers = DeleteNumber(no_repeated_numbers,value[1]) 
    return no_repeated_numbers


no_repeated_numbers= CalculateDifferentTelephoneNumbers(calls,[])
no_repeated_numbers= CalculateDifferentTelephoneNumbers(texts,no_repeated_numbers)
print(no_repeated_numbers)
print("There are {} different telephone numbers in the records.".format(len(no_repeated_numbers)))

