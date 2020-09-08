from RearrangeArrayElements import rearrange_digits,quick_sort

def print_test(test_name,data):
    print("")
    print("---------------------")
    print(test_name)
    sorted_data = quick_sort(data)
    result = rearrange_digits(data)
    if (result is not None):
        size = len(result)
        print("Original input: {}".format(data))
        print("Sorted input by quicksort: {}".format(sorted_data))
        if (size > 1):
            print("Rearranged input: Max {} Min {}".format(result[0],result[1]))
        else:
            print("Rearranged input: {}".format(data,result))
    else:
        print("Invalid input. Can not be sorted.")
    print("")



data = [4, 6, 2, 5, 9, 8]
print_test('Test #1',data)

data = [1,2,3,4,5,6,7,8,9]
print_test('Test #2',data)

data = [9,8,7,6,5,4,3,2,1]
print_test('Test #3',data)

data = None
print_test('Test #4',data)

data = [9,1,8,2,7,3,6,4,5]
print_test('Test #4',data)

data = [1]
print_test('Test #5',data)

