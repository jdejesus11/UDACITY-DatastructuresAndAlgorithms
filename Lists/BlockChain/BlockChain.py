import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
    
    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = (str(self.data) + str(self.timestamp)).encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()
    

class BlockChain(object):
    def __init__ (self):
        self.root = None
        self.tail = None
    
    def add(self,data):
       if (data is not None):
            if (self.root is None and self.tail is None):
                self._add_node_empty_chain(data)
            else:
                    self._add_node_no_empty_chain(data)
    
    def _add_node_empty_chain(self,data):
        timestamp = self.calc_current_datetime_gtm()
        node = Block(timestamp,data,None)
        self.root = node
        self.tail = node
    
    def _add_node_no_empty_chain(self,data):
        while (self.tail.next):
            self.tail = self.next

        node = Block(self.calc_current_datetime_gtm(),data,self.tail.hash)
        self.tail.next = node
        self.tail = node
        
        
    def calc_current_datetime_gtm(self):
        format = '%Y-%m-%dT%H:%M:%SZ'
        return datetime.now().strftime(format)

    def __repr__(self):
        string = ""
        index = 1
        pointer = self.root
        if (pointer is not None):
            while (pointer):
                string+="--------------\n"
                string+=f"Node #: {str(index)}\n"
                string+=f"Data: {str(pointer.data)}\n"
                string+=f"Time stamp: {str(pointer.timestamp)}\n"
                string+=f"Hash: {str(pointer.hash)}\n"
                string+=f"Previous Hash: {str(pointer.previous_hash)}\n"
                pointer = pointer.next
                index+=1
        else:
            string = "<Empty blockchain>"
        return string


