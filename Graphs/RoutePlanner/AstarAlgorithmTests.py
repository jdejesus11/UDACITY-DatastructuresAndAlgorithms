from Data import M
from AstarAlgorithm import shortest_path
import unittest

class TestRouterPlanner(unittest.TestCase):

    def test_path_from_0_to_3(self):
        graph = M()
        initial_index_node = 0
        destination_index_node = 3
        result = shortest_path(graph,initial_index_node,destination_index_node)
        self.assertEqual(result, [0,5,3])
    
    def test_path_no_path_found(self):
        graph = M()
        initial_index_node = 0
        destination_index_node = 8
        result = shortest_path(graph,initial_index_node,destination_index_node)
        self.assertEqual(result, [])
    
    def test_path_from_3_to_3(self):
        graph = M()
        initial_index_node = 3
        destination_index_node = 3
        result = shortest_path(graph,initial_index_node,destination_index_node)
        self.assertEqual(result, [3])

if __name__ == '__main__':
    unittest.main()
