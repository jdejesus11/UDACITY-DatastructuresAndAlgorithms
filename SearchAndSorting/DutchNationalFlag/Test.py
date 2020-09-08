from DutchNationalFlag import DutchNationalFlag

def print_test(test_name,data):
    print(test_name)
    print("")
    dutchNationalFlag = DutchNationalFlag(data)
    dutchNationalFlag.sort()
    print(dutchNationalFlag)
    print("----------------------------------------------")

print_test("Test #1: sorted array input", [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

print_test("Test #3: total unsorted array", [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])

print_test("Test #4: mixed unsorted array", [1,0,1,0,1,0,1,0,1,0,1,0,1,0])

print_test("Test #5: array with repeated numbers", [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

print_test("Test #6: null or None input", None)

print_test("Test #7: Empty input", [])







