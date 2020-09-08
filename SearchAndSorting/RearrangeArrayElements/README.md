DESCRIPTION:
    1.1 Time complexity:
         1.1.1 sorting arrays with quicksort:
               average case: O(n) = n * log (n)
               worst case: O(n) = n ** 2 (if the algo has to swap all elements in each interation)
        1.1.2 selecting max and min combinations:
              average case: O(n) = n (linear). The method selects elements in a single traversal.
        1.1.3 Total time complexity: O(n) = n * log (n) + O(n)

    1.2 Space complexity:
        1.1.1 sorting arrays with quicksort:
               average case: O(n) = O(1) = constant. Sorting is executed in the same array. 
               Only input memory size is need to be allocated.
        1.1.2  selecting max and min combinations:
               average case: O(l) = m (size of bytes of max number) + n (size of bytes of min number)