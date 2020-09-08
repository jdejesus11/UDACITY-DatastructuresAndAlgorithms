DESCRIPTION:
    1.1 Time complexity:
                1.1 Search a letter into each dictionary: (Average case): 0(n) = log(n)
                1.2 Search or find a word (worst case): O(n) = log(n) (search a letter in a dictionary) * n (steps or size of the word)
                1.3 Inserting -Average case-: O(n) = O(1) * n (steps or size of the word)   
                              -Worst case- :  O(n) = O(n) * n (steps or size of the word)  
        
    1.2 Space complexity:
                1.1 Search or find a word:
                    O(n) = O(1) * (word memory size in bytes) + (middle variables * memory size variables of python)
                1.3 Inserting: (trie_node object memory size * n letters or size of the word).
                    Total memory size of trie: dict memory size in bytes of python * n inserted letters  
