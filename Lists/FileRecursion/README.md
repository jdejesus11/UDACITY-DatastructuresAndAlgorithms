DESCRIPTION:
1. This algorithm uses for loop, recursion and os libraries
   to check files with extension .c
    1.1. Time complexity analisis: 
         Each directory can have or not at least 1 directory 
         and many types of files. 
         So this algorithms should check each directory inside any directory
         Time complexity is calculate by taking n levels of directory 
         and m directory inside a i level plus s files in each directory
         O(n) = n * m = y (linear complexity in average case)
   2. Space complexity:
       memory size depends on how many files and directory contains each directory.
       O(n) =  n ( number of files ) * m (number of levels) * m (size in bytes of the variable determined by python) 
            =  (linear space complextiy)
              