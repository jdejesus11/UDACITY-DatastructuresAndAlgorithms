import inspect

#**************************TYPES********************************#
class Node(object):
    def __init__(self):
        self.left = None
        self.rigth = None
        self.first_bit = None
        self.second_bit = None

    def is_a_leaf(self):
        return self.left is None and self.rigth is None

class CharNode(object):
    def __init__(self,char = "",frequency = None):
        self.char = char
        self.frequency = frequency
        self.node = Node()
    
    def compare(self,char_node):
        if (self.frequency < char_node.frequency):
            return -1
        if (self.frequency > char_node.frequency):
            return 1
        else :
            if (self.char is not None and char_node.char is not None):
                if (ord(self.char) < ord(char_node.char)):
                    return -1
        return 0



#************************HELPER CLASSES******************************#
class MinHeap:
    def __init__(self):
        self.data = []
        self.current_size = 0
    
    def insert(self,node):
        self.data.append(node)
        self.current_size += 1
        self.sort()

    def sort(self):
        current_index = self.current_size - 1
        parent_index = current_index // 2
        while (current_index > 0):
            current_tree_node = self.data[current_index]
            parent_tree_node =  self.data[parent_index]
            previous_array_node = self.data[current_index-1]

            #current node has a frequency less than parent node in the heap tree
            if (current_tree_node.compare(parent_tree_node) == -1):
                aux = (parent_tree_node.char,parent_tree_node.frequency , parent_tree_node.node)
                parent_tree_node.char = current_tree_node.char
                parent_tree_node.frequency = current_tree_node.frequency
                parent_tree_node.node = current_tree_node.node
                current_tree_node.char = aux[0]
                current_tree_node.frequency = aux[1]
                current_tree_node.node = aux[2]

            current_index = parent_index
            parent_index = (parent_index // 2)
    
    def pop(self):
        if (self.current_size > 0):
            head = self.data[0]
            popped_element = CharNode(head.char,head.frequency)
            popped_element.node = head.node
            self.data[0] = self.data[-1]
            self.current_size -= 1
            self.data = self.data[1:]
            self._completed_sort()
            return popped_element
        
        return None

    def _completed_sort(self):
        i = 0
        if (self.current_size > 1):
            while (i * 2) < self.current_size:
                next_index = self._next_index(i)
                if (next_index < self.current_size):
                    if (self.data[i].compare(self.data[next_index]) == 1):
                        aux = (self.data[i].char,self.data[i].frequency)
                        self.data[i].char = self.data[next_index].char
                        self.data[i].frequency = self.data[next_index].frequency
                        self.data[next_index].char = aux[0]
                        self.data[next_index].frequency = aux[1]
                i = next_index

    
    def _next_index(self,i):
        if ((i * 2 + 1) >= self.current_size):
            return i * 2
        else:
            if (self.data[i*2].compare(self.data[i*2+1]) == -1):
                if (i > 0):
                    return i * 2 
                else:
                    return 1
            else:
                return i * 2 + 1
    
    def __repr__(self):
        string_rep = ""
        if self.current_size > 0:
            index = 0
            counter = 1
            exponential = 0
            string_rep+="Begin of tree \n"
            while (index < self.current_size):
                string_rep += str(self.data[index].char) + ":" + str(self.data[index].frequency)
                if (2 ** exponential == counter):
                    string_rep+="\n"
                    counter = 1
                    if (exponential == 0):
                        exponential = 1
                    else:
                        exponential*=2
                else:
                    counter +=1
                    string_rep+=" "
                index+=1

            string_rep += "\nEnd of tree"
        else:
            string_rep = "Min heap is empty"
        return string_rep

class HuffmanTree:
    def __init__(self, root = None):
        self.root = root
        self.code_table = None
    
    def generate_table(self):
        if (self.root.node.is_a_leaf() == False):
            self.code_table = self._generate_table(self.root,dict(),"")
        else:
            self.code_table = dict()
            self.code_table[self.root.char] = (self.root.frequency,"0")
    
    def _generate_table(self,node,code_table,code = ""):
        if (node):
            if (node.node.is_a_leaf()):
                code_table[node.char] = (node.frequency,code)
            else:
                left_new_code = code
                if (node.node.first_bit is not None):
                    left_new_code += str(node.node.first_bit)
                code_table = self._generate_table(node.node.left,code_table,left_new_code)
                
                rigth_new_code = code
                if (node.node.second_bit is not None):
                    rigth_new_code += str(node.node.second_bit)
                code_table = self._generate_table(node.node.rigth,code_table,rigth_new_code)
        return code_table
    
    def encode(self,message):
        result = ""
        last_visited = None
        if (self.code_table is not None):
            for item in message:
                if (last_visited is None):
                    value = self.code_table[item]
                    if (value is not None):
                        last_visited = (item,value[1])
                        result+=last_visited[1]
                else:
                    if (item == last_visited[0]):
                        result+=last_visited[1]
                    else:
                        value = self.code_table[item]
                        if (value is not None):
                            last_visited = (item,value[1])
                            result+=last_visited[1]
        return result
    
    def decode(self,data):
        message = ""
        pointer = self.root
        for bit in data:
            if (pointer.node.first_bit == int(bit)):
                    pointer = pointer.node.left
            elif (pointer.node.second_bit == int(bit)):
                    pointer = pointer.node.rigth

            if (pointer.node.is_a_leaf()):
                message+=pointer.char
                pointer = self.root
                     
        return message

#************************ENTRY CLASS*********************************#
class HuffmanCode:
    def __init__(self, message):
        self.message = message
        self.frequencies = None
        self.collection = MinHeap()
        self.huffman_tree = None

    def _calculate_frequencies(self):
        message = self.message
        self.frequencies = dict()
        for char in message:
            value = self.frequencies.get(char)
            if (value is not None):
                self.frequencies[char]=value + 1
            else:
                self.frequencies[char] = 1

        self._convert_frequencies_into_priority_queue()
    
    def _convert_frequencies_into_priority_queue(self):
        for key,value in self.frequencies.items():
            node = CharNode(key,value)
            self.collection.insert(node)

    def huffman_encoding(self):
        if (len(self.message) > 0):
            self._calculate_frequencies()
            first = None
            second = None
            root_node = None
            if (self.collection.current_size > 1):
                while (self.collection.current_size > 1):
                    first = self.collection.pop()
                    second = self.collection.pop()
                    total_frequencies = first.frequency + second.frequency
                    summary_node = CharNode(None,total_frequencies)
                    summary_node.node.first_bit = 0
                    summary_node.node.second_bit = 1
                    summary_node.node.left = first
                    summary_node.node.rigth = second
                    self.collection.insert(summary_node)
                root_node = self.collection.pop()
            else:
                root_node = self.collection.pop()

            self.huffman_tree = HuffmanTree(root_node)
            self.huffman_tree.generate_table()
            result =  self.huffman_tree.encode(self.message)
        else:
            result = "<No data for encoding>"
        return result
        
    def huffman_decoding(self,data):
        if (len(self.message) > 0):
            return self.huffman_tree.decode(data)
        return  "<No data for decoding>"

