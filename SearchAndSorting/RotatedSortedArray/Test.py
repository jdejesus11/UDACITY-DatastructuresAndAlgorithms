from RotateSortedArray import rotated_array_search

def print_test(test_name,number,data):
    print()
    print(test_name)
    result = rotated_array_search(data,number)
    print(f"Index for the {number} is: {result}")
    print()
    print("----------------------------------------------")



print_test("Test #1",1,[6, 7, 8, 9, 10, 1, 2, 3, 4])

print_test("Test #2",6,[6, 7, 8, 9, 10, 1, 2, 3, 4])

print_test("Test #3",8,[6, 7, 8, 1, 2, 3, 4])

print_test("Test #4",10,[6, 7, 8, 1, 2, 3, 4])

print_test("Test #5",1534,[6, 7, 8, 1, 2, 3, 4])

data = []
for value in range(0,900):
    data.append(value)
for value in range(900,10000):
    data.append(value)
print_test("Test 4: Index of 1534 in big dataset",1534,data)





