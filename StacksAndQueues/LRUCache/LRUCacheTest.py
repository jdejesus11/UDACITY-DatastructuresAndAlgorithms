import time
from LRUCache import LRUCache

"""
TEST #1: INSERT ELEMENTS UNTIL CACHE GETS FULL
"""
print("Test #1: INSERT ELEMENTS UNTIL CACHE GETS FULL.")
capacity = 5
cache_test_1 = LRUCache(capacity)
for key in range(capacity+1):
    value = key
    cache_test_1.set(key, value)

print(cache_test_1)
print("-----------------------------------------------")

"""
TEST #2: INSERT ELEMENT WHEN CHACHE IS FULL
"""
print("")
print("Test #2: INSERT AN ELEMENT WHEN CACHE IS FULL.")
print("Element with key #1 should be deleted")
extra_element_key = capacity+1  # extra_element equals to 6
extra_element_value = capacity + 1
cache_test_1.set(extra_element_key,extra_element_value)
print(cache_test_1)
print("-----------------------------------------------")

"""
TEST #3: TRYING TO GET AN ELEMENT WHICH IS NOT INSIDE CACHE
"""
print("")
print("TEST #3: TRYING TO GET AN ELEMENT WHICH IS NOT INSIDE CACHE")
print("-1 should be printed.")
key = capacity*10
print(f"Looking value for given key: {key}")
desired_element = cache_test_1.get(key)
print("Desired value: " + str(desired_element))
print("-----------------------------------------------")

"""
TEST #4: TRYING TO GET AN ELEMENT WHICH IS NOT INSIDE CACHE
"""
print("")
print("TEST #4: TRYING TO GET AN ELEMENT WHICH IS NOT INSIDE CACHE")
print("-1 should be printed.")
key = -1*capacity*10
print(f"Looking value for given key: {key}")
desired_element = cache_test_1.get(key)
print("Desired value: " + str(desired_element))
print("-----------------------------------------------")

"""
TEST #5: TRYING TO GET AN ELEMENT WHERE CACHE IS EMPTY
"""
cache_test_5 = LRUCache()
print("")
print("TEST #5: TRYING TO GET AN ELEMENT WHERE CACHE IS EMPTY")
print("-1 should be printed.")
key = 1
print(f"Looking value for given key: {key}")
desired_element = cache_test_1.get(key)
print("Desired value: " + str(desired_element))
print("-----------------------------------------------")

"""
TEST #6: TRYING TO SET AN ELEMENT WHICH KEY HAS ALREADY BEEN SET
"""
capacity = 3
cache_test_6 = LRUCache(5)
print("")
print("TEST #6: TRYING TO SET AN ELEMENT WHICH KEY HAS ALREADY BEEN SET")
key = 1
value = 1
cache_test_6.set(key,value)

key_2 = 1
value_2 = 2
cache_test_6.set(key_2,value_2)
print(cache_test_6)
print("-----------------------------------------------")


"""
TEST #7: TIME EXECUTION. (PLEASE, SET CAPACITY TO HIGH VALUE SO THAT YOU CAN SEE TIME EXECUTION)
"""
capacity = 100
cache_test_7 = LRUCache(capacity)
start = time.time()
for key in range(capacity):
    value = key
    cache_test_7.set(key,value)
end = time.time()
print(cache_test_7)
print(f"Inserting time: {end - start}")
print("-----------------------------------------------")

    