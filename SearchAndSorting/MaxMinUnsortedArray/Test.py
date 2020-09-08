import random
from MaxMinUnsortedArray import get_min_max

def generate_ramdom_data(min,max):
    input = [i for i in range(min, max)]  # a list containing 0 - 9
    random.shuffle(input)
    return input

def print_test(test_name,input):
    print("")
    print(test_name)
    result = get_min_max(input)
    print("Original input: {}".format(input))
    if (result is not None):
        print("Max: {} Min: {}".format(result[1], result[0]))
    else:
        print("No result")


data = generate_ramdom_data(5,10)
print_test("Test #1: ", data)

data = [1,1,1,1,1,1]
print_test("Test #2: ", data)

data = [1,1,1,1,1,1]
print_test("Test #3: ", data)

data = [4,2,4,4,8]
print_test("Test #4: ", data)

data = []
print_test("Test #5: ", data)

data = None
print_test("Test #6: ", data)






