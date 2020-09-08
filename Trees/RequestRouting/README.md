DESCRIPTION:
    1.1 Time complexity:
                1.1 Search a word into each dictionary: (Average case): 0(n) = log(n)
                1.2 Search or find a complete path (worst case): O(n) = log(n) (search a word in dictionary) * n (steps or size of the path)
                1.3 Inserting -Average case-: O(n) = O(1) * n (steps or size of the path) + 
                               extra operations (i.e: splitting the string into an array)
                              -Worst case- :  O(n) = O(n) * n (steps or size of the path)  
                               extra operations (i.e: splitting the string into an array) +
    1.2 Space complexity:
                1.1 Search or find a path:
                    O(n) = O(1) * (a path memory size in bytes) + (middle variables * memory size variables of python)
                           +  extra operations (i.e: converted string into array)
                1.3 Inserting: -Average case-: trie_node object memory size * n routes or n elements of the path)
                                +  extra operations (i.e: converted string into array)
                                Total memory size of trie: dict memory size in bytes of python * n inserted path  
