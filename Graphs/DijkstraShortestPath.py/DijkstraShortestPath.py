import math
from heapq import heappush,heappop
from Data import data

# Helper Class
class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance
    

# Helper Classes
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

class Graph(object):
    def __init__(self, node_list = []):
        self.nodes = node_list

    # adds an edge between node1 and node2 in both directions
    def add_edge(self, node1, node2, distance):
        if node1 not in self.nodes and node2 not in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)
    
    def initNodes(self):

        node_u = GraphNode('U')
        node_d = GraphNode('D')
        node_a = GraphNode('A')
        node_c = GraphNode('C')
        node_i = GraphNode('I')
        node_t = GraphNode('T')
        node_y = GraphNode('Y')

        self.add_edge(node_u, node_a, 4)
        self.add_edge(node_u, node_c, 6)
        self.add_edge(node_u, node_d, 3)
        self.add_edge(node_d, node_c, 4)
        self.add_edge(node_a, node_i, 7)
        self.add_edge(node_c, node_i, 4)
        self.add_edge(node_c, node_t, 5)
        self.add_edge(node_i, node_y, 4)
        self.add_edge(node_t, node_y, 5)

        self.nodes.append(node_u)
        self.nodes.append(node_d)
        self.nodes.append(node_a) 
        self.nodes.append(node_c) 
        self.nodes.append(node_i) 
        self.nodes.append(node_t)  
        self.nodes.append(node_y)  

    
    def find_nodes(self,node_name):
        data =  list(filter(lambda element: element.value == node_name, self.nodes))
        if (len(data) == 1):
            data = data[0] 
            return data

        return None

class HeapNode():
    def __init__(self,node,distance):
        self.node = node
        self.distance = distance
    
    def __lt__(self, other):
        return self.distance < other.distance



def dijkstra(graph, init_node_value, end_node_name):

    priority_queue = []
    visited_nodes = []
    path_nodes = []
    min = None

    start_node = graph.find_nodes(init_node_value)
    end_node = graph.find_nodes(end_node_name)

    heappush(priority_queue,HeapNode(start_node,0))

    while (len(priority_queue) > 0):
        head = heappop(priority_queue)
        if (head.node.value != end_node.value):
            min=head.distance
            visited_nodes.append(head.node.value)
            for vertice in head.node.edges:
                if (vertice.node.value not in visited_nodes):
                    priority_head = None
                    for i in range(len(priority_queue)):
                        if (priority_queue[i].node.value == vertice.node.value):
                            priority_head = priority_queue[i]
                            break
                    if (priority_head is not None):
                        if (vertice.distance + head.distance < priority_head.distance ):
                            priority_head.distance = vertice.distance + head.distance
                    else: 
                        heappush(priority_queue,HeapNode(vertice.node,head.distance + vertice.distance))
        else:
            min = head.distance
            break
     

    return min
    pass




