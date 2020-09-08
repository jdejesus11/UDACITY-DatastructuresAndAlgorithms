from collections import deque

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

class GroupOperations(object):
  
    def is_user_in_group(self,user, group):
        return self._is_user_in_group(user,group,[])

    def _is_user_in_group(self,user,group,visited_cache):
        """
        Return True if user is in the group, False otherwise.

        Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
        """
        if (group.name not in visited_cache):
           users = group.get_users()
           if (user in users):
               return True
           else:
                visited_cache.append(group.get_name())
                related_groups = group.get_groups()
                for g in related_groups:
                    partial_result = self._is_user_in_group(user,g,visited_cache)
                    if (partial_result == True):
                        return partial_result

        return False

