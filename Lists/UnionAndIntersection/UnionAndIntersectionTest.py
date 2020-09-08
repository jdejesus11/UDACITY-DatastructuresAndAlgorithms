from UnionAndIntersection import Node,LinkedList

print("-----------------------------------------------")
print("TEST #1: GET UNION AND INTERSECTION")
"""
TEST #1: GET UNION AND INTERSECTION
"""
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

joined_items = linked_list_1.union(linked_list_2)
if (joined_items.size() > 0):
    print("Joined elements:")
    print(joined_items)
else:
    print("There are no joined elements.")
intersected_items = linked_list_1.intersection(linked_list_2)
if (intersected_items is not None):
    if (intersected_items.size() > 0):
        print("Intersected elements:")
        print(intersected_items)
    else:
         print("There are no intersected elements.")
else:
    print("There are no intersected elements.")

print()
print("-----------------------------------------------")
print("TEST #2: GET UNION AND INTERSECTION BETWEN A LIST AND AN EMPTY LIST")
"""
TEST #2: GET UNION AND INTERSECTION BETWEN A LIST AND AN EMPTY LIST
"""
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

joined_items = linked_list_1.union(linked_list_2)
if (joined_items.size() > 0):
    print("Joined elements:")
    print(joined_items)
else:
    print("There are no joined elements.")
intersected_items = linked_list_1.intersection(linked_list_2)
if (intersected_items is not None):
    if (intersected_items.size() > 0):
        print("Intersected elements:")
        print(intersected_items)
    else:
         print("There are no intersected elements.")
else:
    print("There are no intersected elements.")

print()
print("-----------------------------------------------")
print("TEST #3: GET UNION AND INTERSECTION BETWEN TWO EMPTY LIST")
"""
TEST #3: GET UNION AND INTERSECTION BETWEN TWO EMPTY LIST
"""
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

joined_items = linked_list_1.union(linked_list_2)
if (joined_items.size() > 0):
    print("Joined elements:")
    print(joined_items)
else:
    print("There are no joined elements.")
intersected_items = linked_list_1.intersection(linked_list_2)
if (intersected_items is not None):
    if (intersected_items.size() > 0):
        print("Intersected elements:")
        print(intersected_items)
    else:
         print("There are no intersected elements.")
else:
    print("There are no intersected elements.")

print()
print("-----------------------------------------------")
print("TEST #4: GET UNION AND INTERSECTION BETWEN TWO DIFFERENTS LISTS")
"""
TEST #4: GET UNION AND INTERSECTION BETWEN TWO DIFFERENTS LISTS
"""
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,3,4,5]
element_2 = [6,7,8,9]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

joined_items = linked_list_1.union(linked_list_2)
if (joined_items.size() > 0):
    print("Joined elements:")
    print(joined_items)
else:
    print("There are no joined elements.")
intersected_items = linked_list_1.intersection(linked_list_2)
if (intersected_items is not None):
    if (intersected_items.size() > 0):
        print("Intersected elements:")
        print(intersected_items)
    else:
         print("There are no intersected elements.")
else:
    print("There are no intersected elements.")

