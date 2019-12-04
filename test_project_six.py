import unittest
import project_six

class Testp6(unittest.TestCase):

    def generate_graph(self):
        g = project_six.graph(4, False, False)
        g.insert_vertex(0)
        g.insert_vertex(1)
        g.insert_vertex(2)
        g.insert_vertex(3)
        g.insert_edge(0, 3, None)
        g.insert_edge(1, 4, None)
        g.insert_edge(2, 2, None)
        g.insert_edge(3, 3, None)

        return g

    def test_KruskalsAlg(self):
        g = self.generate_graph()
        self.assertEqual(project_six.kruskal_alg(g), 0) 
        self.assertEqual(project_six.kruskal_alg(g), 0) 
        self.assertEqual(project_six.kruskal_alg(g), 0)
        self.assertEqual(project_six.kruskal_alg(g), 0)
        self.assertEqual(project_six.kruskal_alg(g), 0)
    
    def test_topologicalSort(self):
        g = self.generate_graph()
        self.assertEqual(project_six.topological_sort(g), 0)
        self.assertEqual(project_six.topological_sort(g), 0)
        self.assertEqual(project_six.topological_sort(g), 0)
        self.assertEqual(project_six.topological_sort(g), 0)
        self.assertEqual(project_six.topological_sort(g), 0)
        


if __name__ == "__main__":
    unittest.main()