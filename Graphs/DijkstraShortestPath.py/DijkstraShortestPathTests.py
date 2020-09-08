from DijkstraShortestPath import Graph, dijkstra, HeapNode
from Data import data
import unittest

class DijkstraShortestPathTests(unittest.TestCase):

    def test_path_from_A_to_U(self):
        graph = Graph()
        initial_name_node = 'U'
        end_name_node = 'A'
        min_cost = 4
        result = dijkstra(graph,initial_name_node,end_name_node)
        self.assertEqual(result, min_cost)
    
    def test_path_from_A_to_A(self):
        graph = Graph()
        initial_name_node = 'A'
        end_name_node = 'A'
        min_cost = 0
        result = dijkstra(graph,initial_name_node,end_name_node)
        self.assertEqual(result, min_cost)
    


if __name__ == '__main__':
    unittest.main()

