from SquareRoot import sqrt

def print_test(test_name,number):
    print()
    print(test_name)
    result = sqrt(number)
    print(f"Square root for {number} is: {result}")
    print("----------------------------------------------")
    print()


print_test("Test #1: Square root of 1",1)

print_test("Test #2: Square root of 3",3)

print_test("Test #3: Square root of 27",27)

print_test("Test #4: Perfect square root of 100",100)

print_test("Test #5: Non perfect square root of 1000",1000)

print_test("Test #6: Perfect square root of a big number 10000000000",10000000000)

print_test("Test #7: Square root of 0",0)





