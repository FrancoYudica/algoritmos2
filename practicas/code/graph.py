from typing import List, Dict


class GraphNode:
    def __init__(self, key):
        self.key = key


class BFSNode(GraphNode):
    def __init__(self, key) -> None:
        super().__init__(key)
        self.added = False
        self.depth = 0


class Graph:
    
    def __init__(self, n) -> None:
        # n is the number of vertices of the graph
        self.n = n

        # The data is stored inside a dictionary / hashtable
        self._data : Dict[List[GraphNode]] = {}

    @classmethod
    def initialize(cls, vertices, pairs):
        # vertices: list(vertex)
        # pairs: list(vertex0, vertex1), adjacent vertices
        graph = Graph(len(vertices))
        
        # Inserts all the vertices
        for vertex in vertices:
            graph.insert(vertex)

        # Creates the vertices links
        for (vertex0, vertex1) in pairs:
            graph.link(vertex0, vertex1)

        return graph
    
    @property
    def vertices(self):
        return list(self._data.keys())
    
    @property
    def pairs(self):
        # Returns a list of tuple, containing all the pairs of the graph
        pairs_list = []
        already_added = {}

        for vertex in self._data:

            already_added[vertex] = True 
            for adjacent_vertex in self._data[vertex]:
                
                if adjacent_vertex in already_added:
                    continue
                
                pairs_list.append((vertex, adjacent_vertex))

        return pairs_list
    
    def insert(self, vertex):
        if len(self._data) == self.n:
            raise Exception("The graph is full, only {self.n} vertices allowed")
        # Adds the new vertex to data
        if vertex in self._data:
            raise Exception(f"Vertex: {vertex} already added")
        
        # Initializes the adjacency list
        self._data[vertex] = []

    def link(self, vertex0, vertex1):
        # Links the verties
        self._data[vertex0].append(vertex1)
        self._data[vertex1].append(vertex0)

    def exists_path(self, vertex0, vertex1):
        """Returns if there is a path that connects the vertices"""
        # Uses a similar algorithm to Breadth-First-Search
        
        traversed_keys = {}
        
        queue = [vertex0]

        while len(queue) > 0:
            vertex = queue.pop(0)

            if vertex == vertex1:
                return True

            # Stores the traversed vertex in a dictionary
            traversed_keys[vertex] = None

            # Loops throught all the adjacent vertices and adds them to the queue
            adjacent_vertices = self._data[vertex]
            for adjacent_vertex in adjacent_vertices:

                # If the vertex wasn't added to the queue, adds
                if adjacent_vertex not in traversed_keys:
                    queue.append(adjacent_vertex)

        return False
    
    def is_connected(self):
        """Returns if there exists a path for all the vertiec"""