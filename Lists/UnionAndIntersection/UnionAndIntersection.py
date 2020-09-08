class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def union(self,llist_2):
        joined_list = LinkedList()
        pointer_1 = self.head
        pointer_2 = llist_2.head
        while (pointer_1 or pointer_2):
            if (pointer_1):
                joined_list.append(pointer_1.value)
                pointer_1 = pointer_1.next
            if (pointer_2):
                joined_list.append(pointer_2.value)
                pointer_2 = pointer_2.next
        return joined_list
        pass

    def intersection(self,llist_2):

        result = LinkedList()

        if (llist_2 is None):
            return None

        if (self.head is None or llist_2.head is None):
            return None

        if (self.size() > llist_2.size()):
            aux = self.head
            self.head = llist_2.head
            llist_2.head = aux

        pointer_1 = self.head
        while (pointer_1):
            pointer_2 = llist_2.head
            while (pointer_2):
                if (pointer_2.value is not None):
                    if (pointer_1.value == pointer_2.value):
                        result.append(pointer_1.value)
                        pointer_2.value = None
                pointer_2 = pointer_2.next
            pointer_1 = pointer_1.next
        return result




    