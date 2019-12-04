#Create on 11/12/19 by: Adrian Lopez 
#Project 6; Data Structures 2302, Instructor: Diego Aguirre, T.A: Gerardo Barraza
#Purpose: implement the following graph algorithms; Kruskal's algorithm, and Topological sort

from queue import Queue

class DisjointSetForest:
    def __init__(self, n):
        self.forest = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index < len(self.forest)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.forest[a] < 0:
            return a

        return self.find(self.forest[a])

    def find_contains_loop(self, a, s=None):
        if not self.is_index_valid(a):
            return -1

        if s is None:
            s = set()

        if a in s:
            print("Loop found")
            return -1

        s.add(a)

        if self.forest[a] < 0:
            return a

        return self.find_contains_loop(self.forest[a], s)

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:  # Problems 3 and 4
            self.forest[rb] = ra

    def in_same_set(self, a, b):
        if not self.is_index_valid(a) or not self.is_index_valid(b):
            return False

        return self.find(a) == self.find(b)

    def num_sets(self):
        count = 0

        for k in self.forest:
            if k < 0:
                count += 1

        return count

    def is_equal(self, dsf):

        if len(self.forest) != len(dsf.forest):
            return False

        # Running time O(n^2). Can you do it in O(n)? (:
        for i in range(len(self.forest)):
            for j in range(len(self.forest)):
                if self.in_same_set(i, j) != dsf.in_same_set(i, j):
                    return False

        return True

    def __str__(self):
        return str(self.forest)

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight

class graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed=False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
    
    def insert_vertex(self):
        self.al.append([])

        return len(self.al) - 1  # Return id of new vertex

    def insert_edge(self, source, dest, weight=1):
        if not self.is_valid_vertex(source) or not self.is_valid_vertex(dest):
            print('Error, vertex number out of range')
        elif weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest, weight))
            if not self.directed:
                self.al[dest].append(Edge(source, weight))
    
    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)
    
    def compute_indegree_every_vertex(self, v):
        if not self.is_valid_vertex(v) or not self.is_valid_vertex(v):
            return 
        
        return len(self.al[v])
    
    def kruskal_alg(self, graph):
        T = set()
        edges = set()
        for i in range(graph.vertices):
            for j in range(graph.vertices):
                if graph.graph[i][j] != 0 and (j, i) not in edges:
                    edges.add((i, j))
        sorted_edges = sorted(edges, key=lambda e:graph.graph[e[0]][e[1]])
        union = graph.union(graph.vertices)
        for e in sorted_edges:
            u, v = e
            if union.connected(u, v):
                continue
            union.graph.union(u, v)
            T.add(e)
        return T
    
    def topological_sort(self, graph):
        all_in_degrees = self.compute_indegree_every_vertex(graph)
        sort_result = []

        q = Queue()

        for i in range(len(all_in_degrees)):
            if all_in_degrees[i] == 0:
                q.put(i) #enqueue
        
        while not q.empty():
            u = q.get() #dequeue

            sort_result.append(u)

            for adj_vertex in graph.get_adj_vertices(u):
                all_in_degrees[adj_vertex] -= 1

                if all_in_degrees[adj_vertex] == 0:
                    q.put(adj_vertex)
        
        if len(sort_result) != graph.num_vertices: #cycle found
            return None
        
        return sort_result
    
    

