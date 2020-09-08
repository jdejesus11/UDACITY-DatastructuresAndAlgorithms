class TrieNode:
    def __init__(self):
        self.children = dict()
    
    def insert(self, char):
        pass
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        head = self.root
        tail = head
        for char in word:
           value = tail.children.get(char)
           if (value is None):
                node = TrieNode()
                tail.children[char] = node 
           tail = tail.children[char] 
        pass  
        
    def find(self, prefix):
        result = []
        head = self.root
        index = 0
        size = len(prefix)
        if (prefix is not None):
            if (size > 0):
                while (index < size):
                    char = prefix[index]
                    char_in_trie = head.children.get(char)
                    if (char_in_trie is not None):
                        head = char_in_trie
                        index+=1
                    else:
                        break
                if (index == size):
                    result = self._find(head)

        return result

    def _find(self,tail):
         result = []
         for item in tail.children.items():
             subresult =  self._find(item[1])
             subresult = [ item[0] + subitem  for subitem in subresult]
             if (len(subresult) == 0):
                 subresult = [item[0]]
             result+=subresult

         return result
    
    def __repr__(self):
        string = ""
        tail = self.root
        data = self._find(tail)
        print(data)
        return string

       




        