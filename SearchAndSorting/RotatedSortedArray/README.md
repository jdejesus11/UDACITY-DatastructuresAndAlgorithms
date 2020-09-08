DESCRIPTION:
    1.1 Time complexity:
        0(n) = O(n/2) =  Log(n)
        Binary search was applied to find the index of any number.
        This algo can find two edge cases: 
            When the middle is greater thant both sides elements.
            Whent the middle is less thant both sides elements.
            In each case, this algo is appplied again for each side of the middle.
        

    1.2 Space complexity:
        0(n) = n = Linear
        This algo uses pointer to iterate recursively over the array, and
        it does not modify or create new array from the original array.


