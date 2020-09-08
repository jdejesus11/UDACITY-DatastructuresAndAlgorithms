DESCRIPTION:
1. This algorithm uses a dictionary to persist main key and values, which time complexity is O(n) = Log(n).
    1.1. Time complexity analysis: 
         1.1.1 Get, Set/Put, Pop in average case for a dict is equal to O(I) = constant time.
         1.1.2 Worst case is equal to O(n) = linear time
    1.2 Space complexity analysis:
         1.2.1 The worse case is when the cache is full. In this case, for n elements inside the cache,
               space complextity is
               O(n) = capacity (entered by the user) * m (size in bytes of each item determined by python) +
                       local variables * m (size in bytes of each item determined by python) 
                    = linear complexity
2. In order to track recent and oldest items, hence, a queue is implemented to save keys in order as they are inserted, so
    oldest keys are on top of the queue and can be popped and delete the item in the dict when the cache is full.
    2.1 Time complexity analisis:
        2.1.1 Deleting an item from the dict using Pop in average case is O(I) = constant time.
        2.1.1 Popping elements from a queue takes O(I) = constant time.
