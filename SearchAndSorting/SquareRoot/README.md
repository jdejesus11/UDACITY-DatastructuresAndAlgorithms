DESCRIPTION:
    1.1 Time complexity:
        0(n) = O(n/2) =  Log(n)
        Binary search was applied to find square root of any number.
        This code selects the middle of two numbers and checks if the square of the middle
        is least, equal or greater than the number. This process is repeated 
        until a perfect square root or a closer value is found.
        

    1.2 Space complexity:
        0(n) = O(1) = Constant = This only needs pointers allocations.
                               = pointer * memory size in bytes allocated by python * n pointers or auxiliar variables.
