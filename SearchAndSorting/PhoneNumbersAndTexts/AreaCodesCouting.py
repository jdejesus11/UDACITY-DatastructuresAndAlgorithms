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

def get_area_code(number):
  number_type = -1
  area_code = ""
  opening_symbol = "("
  closing_simbol = ")"
  mobile_symbol = " "
  telemarket_symbol = "140"
  index = 0
  if (number[0] == opening_symbol):
      number_type = 1
      index = 1
  while True:
       if (index >= len(number)):
          break;
       if (number_type == 1 and number[index] == closing_simbol):
          break;
       if (number[index] == mobile_symbol):
            number_type = 2
            break;
       if (area_code == telemarket_symbol):
           number_type = 3
           break
       else:
         area_code+=str(number[index])
       index+=1
  return str(area_code),number_type


def get_called_numbers_from_bangalore(calls):
    from_bangalore_to_bangalore_number = 0
    from_bangalore_to_elsewhere_number= 0
    bangalore_area_code = "080"
    called_people = []
    emitter_phonenumber = None
    receiver_phonenumber = None
    code = None
    for call in calls:
      emitter_phonenumber = call[0]
      receiver_phonenumber = call[1]
      code = get_area_code(emitter_phonenumber)
      if (code[1] == 1 and code[0] == bangalore_area_code):
          from_bangalore_to_elsewhere_number+=1
          code = get_area_code(receiver_phonenumber)
          if (code[1] != 3):
              if (code[0] == bangalore_area_code):
                  from_bangalore_to_bangalore_number+=1
              if (code[0] not in called_people):
                  called_people.append(code[0])

    return called_people,from_bangalore_to_bangalore_number,from_bangalore_to_elsewhere_number

def calculate_percentage(value_a,value_b):
   return float(float(value_a)/float(value_b))*100

#---------------------------------PART A-------------------------------------------#
print("The numbers called by people in Bangalore have codes:")
result = get_called_numbers_from_bangalore(calls)
numbers = result[0]
numbers.sort()
for x in numbers:
  print(x)


#---------------------------------PART B-------------------------------------------#
percentage = calculate_percentage(result[1],result[2])
message = "{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage)
print(message)

