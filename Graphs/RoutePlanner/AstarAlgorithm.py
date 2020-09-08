
from heapq import heappush,heappop
import math

class Node():
    def __init__(self,value,cost,initial_path):
        self.value = value
        self.cost = cost
        self.path = initial_path
    
    def __str__(self):
        return   str(self.value[0]) + " " + str(self.value[1]) + " " + str(self.cost)

    def __lt__(self, other):
        return self.cost < other.cost

def calculate_distance(coord1,coord2):
    dx = abs(coord1[0] - coord2[0])
    dy = abs(coord1[1] - coord2[1])
    return  math.sqrt(dx * dx + dy * dy)


def is_valid_coords(intersection,roads,start,goal):
    result = True
    if (start < 0 or start >= len(intersection)):
        result = False
    
    if (goal < 0 or goal >= len(roads)):
        result = False

    return result

def shortest_path(M,start,goal):
    path = []
    if (is_valid_coords(M.intersections,M.roads,start,goal)):
        priority_queue = []
        visited_nodes = []
        
        coord_dest = M.intersections[goal]
        coord = (M.intersections[start][0],M.intersections[start][1])
        head_node =   Node(coord,0,[start])
        heappush(priority_queue,head_node)
        current_intersection = None
        non_visited_nodes = None
        
        while (priority_queue):
            current_intersection = heappop(priority_queue)
            current_id = current_intersection.path[-1]
            visited_nodes.append(current_id)
            
            current_roads =  M.roads[current_id] if current_id >=0 and current_id < len(M.roads) else None
            
            non_visited_nodes = 0
            for current_road in current_roads:
                if (current_road not in visited_nodes):
                    current_road_coord = M.intersections[current_road]
                    current_road_distance = calculate_distance(current_road_coord,current_intersection.value)
                    current_road_distance_to_dest = calculate_distance(current_intersection.value,coord_dest)
                    current_path = current_intersection.path + [current_road]
                    child_node = Node(current_road_coord, current_intersection.cost + current_road_distance + current_road_distance_to_dest, current_path )
                    heappush(priority_queue,child_node)

            if (coord_dest[0] == M.intersections[current_id][0] and coord_dest[1] == M.intersections[current_id][1]):
                if (non_visited_nodes == 0):
                    path = current_intersection.path
                    break

    return path
    pass





    