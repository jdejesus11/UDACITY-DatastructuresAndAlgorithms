class RouteTrieNode:
    def __init__(self):
        self.children = dict() 
        self.handler = None

class RouteTrie:
    def __init__(self,root_handler_name,not_found_router_name = "Not found"):
       self.root = RouteTrieNode()
       self.root.handler = root_handler_name
       self.config_404_path(not_found_router_name)

    
    def config_404_path(self,handler_name):
       self.insert(["error","404"],handler_name)

    def insert(self,path_list,handler_name):
        head = self.root
        tail = head
        last_item_index = len(path_list) - 1
        size = len(path_list)
        for index, path in enumerate(path_list):
            value = tail.children.get(path)
            if (value is None):
                    node = RouteTrieNode()
                    tail.children[path] = node
                    if (index == last_item_index):
                        node.handler = handler_name
            tail = tail.children[path] 
        pass  

    def find(self,path_list):
        tail = self.root
        return self._find(tail,path_list)
    
    def _find(self,tail,path_list):
         result = None
         tail = self.root
         last_item_index = len(path_list) - 1
         size = len(path_list)

         if (size == 1):
             value = path_list[0]
             if (value != "/"):
                 is_value_root = tail.children.get(value) 
                 if (is_value_root is not None):
                     result = tail.handler
             else:
                result = tail.handler
         else:
            for index,path in enumerate(path_list):
                sub_tail = tail.children.get(path)
                if (sub_tail is not None):
                    tail = sub_tail
                    result = sub_tail.handler
                else:
                    result = None
                    break
    
         return result
    
    def _find_all(self,tail):
         result = []
         for item in tail.children.items():
             subresult =  self._find_all(item[1])
             subresult = [ item[0] + "/" + subitem  for subitem in subresult]
             if (len(subresult) == 0):
                 subresult = [item[0]]
             result+=subresult

         return result
    
    def __repr__(self):
        string = ""
        tail = self.root
        data = self._find_all(tail)
        return "\n".join(data)



# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self,root_handler_name,not_found_router_name):
        self.routes = RouteTrie(root_handler_name,not_found_router_name)

    def add_handler(self,path,handler_name):
        path_list = self.split_path(path)
        self.routes.insert(path_list,handler_name)
        
    def lookup(self,path):
        result = self._find_404_not_found()
        if (path is not None):
            path_list = self.split_path(path)
            sub_result = self.routes.find(path_list)
            if (sub_result is not None):
                result = sub_result

        return result
        pass

    def split_path(self,path):
        result = []
        if (path == "/"):
            result = ["/"]
        else:
            result = path.split("/")
            result = [ path  for path in result if (path != "")  ]
        return result
    
    def _find_404_not_found(self):
        return self.routes.find(["error","404"])
    





