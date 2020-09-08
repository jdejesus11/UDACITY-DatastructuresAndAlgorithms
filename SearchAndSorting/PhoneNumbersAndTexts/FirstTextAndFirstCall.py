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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_texts_record = texts[0]
texts_message = "First record of texts, {} texts {} at time {}".format(
                                                                 first_texts_record[0],
                                                                 first_texts_record[1],
                                                                 first_texts_record[2])
print(texts_message)

last_calls_record = calls[0]
calls_message="Last record of calls, {} calls  {} at time {}, lasting {} seconds".format(
                                                                                   last_calls_record[0],
                                                                                   last_calls_record[1],
                                                                                   last_calls_record[2],
                                                                      last_calls_record[3]) 
print(calls_message)





