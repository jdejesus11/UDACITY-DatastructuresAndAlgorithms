from ActiveDirectory import GroupOperations
from ActiveDirectory import Group
import time

print("-----------------------------------------------")
"""
TEST #1: GET AN USER. RETURN NONE.
"""
print("TEST #1: GET AN USER. RETURN NONE.")
print()
group = Group("Admin")
group_child = Group("Family")
group_child_2 = Group("Company")
group_child_3 = Group("Shared")

user_1 = "Juan"
user_2 = "Sandra"
user_3 = "Andrea"
user_4 = "Julio"

group_child_2.users.append(user_1)
group_child_2.users.append(user_2)
group_child_2.users.append(user_3)

group_child_3.users.append(user_4)

group_child_2.add_group(group_child_3)
group_child.add_group(group_child_2)
group_child.add_group(group_child_3)
group.add_group(group_child)

operation = GroupOperations()
user_name = "Ana"
result = operation.is_user_in_group(user_name,group)
if (result):
    print(f"{user_name} was found inside {group.get_name()}")
else:
    print(f"{user_name} was not found inside {group.get_name()}")

print("-----------------------------------------------")
"""
TEST #2: GET AN USER. RETURN USER.
"""
print("TEST #2: GET AN USER. RETURN USER.")
print()
group = Group("Admin")
group_child = Group("Family")
group_child_2 = Group("Company")
group_child_3 = Group("Shared")

user_1 = "Juan"
user_2 = "Sandra"
user_3 = "Andrea"
user_4 = "Julio"

group_child_2.users.append(user_1)
group_child_2.users.append(user_2)
group_child_2.users.append(user_3)

group_child_3.users.append(user_4)

group_child_2.add_group(group_child_3)
group_child.add_group(group_child_2)
group_child.add_group(group_child_3)
group.add_group(group_child)

operation = GroupOperations()
user_name = "Sandra"
result = operation.is_user_in_group(user_name,group)
if (result):
    print(f"{user_name} was found inside {group.get_name()}")
else:
    print(f"{user_name} was not found inside {group.get_name()}")
print("-----------------------------------------------")