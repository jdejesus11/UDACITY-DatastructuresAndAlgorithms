from collections import deque

class LRUCache(object):
    def __init__(self, capacity = None):
        self.keys = deque()
        self.table = dict()
        self.capacity = capacity
        self.default_no_empty = -1
        pass

    def get(self, key):
        result = self.table.get(key)
        if (result is not None):
            return result
        return self.default_no_empty
        pass

    def set(self, key, value):
        is_full = self.is_full()
        if (is_full is False):
            result = self.get(key)
            if (result == self.default_no_empty):
                self.table[key] = value
                self.keys.appendleft(key)
            else:
                self.table[key] = value
        else:
            key_to_be_deleted = self.keys.pop()
            self.table.pop(key_to_be_deleted,self.default_no_empty)
            self.set(key,value)
        pass

    def is_full(self):
        return len(self.table) >= self.capacity
    
    def __repr__(self):
        if len(self.table) > 0:
            print("")
            s = "<LEAST RECENT ELEMENT>\n_________________\n" 
            s += "\n_________________\n".join(["Key:"+str(index) + " " + "Value:"+str(self.table[index]) for index in self.table])
            s += "\n_________________\n<MOST RECENT ELEMENT>"
            return s
        else:
            return "<cache is empty>"
    
    


