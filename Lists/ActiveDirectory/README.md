DESCRIPTION:
1. Time complexity: This algorithm has many cases:
    1.1 If the user does not belong to any group,
        it has to search each group.
        Caching visited groups will speed the seearching up.
        Average case: O(n) = n = linear time 
2. Space complexity:
       memory size depends on how many files and directory contains each directory.
       O(n) =  n ( number of users ) * m (number of groups) * m (size in bytes of the variable determined by python) 
            =    (linear space complextiy)
              

