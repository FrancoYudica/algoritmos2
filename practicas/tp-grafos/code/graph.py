from typing import List, Dict


class GraphNode:
    def __init__(self, key):
        self.key = key

    def __repr__(self) -> str:
        return f"Node({self.key})"

class _NodeData:
    # This class shouldn't be used outside this file
    """Contains the GraphNode and it's adjacent Nodes"""
    def __init__(self, node: GraphNode):
        self.node = node

        # Initializes as empty list
        self.adjacent : List[_NodeData] = []

class Graph:
    
    """
    Graph structure
    _data is a dictionary, where the keys are the keys of the nodes
    and the values are the _NodeData instances
    {
        key0 : _NodeData[node, adjacency_list],
        key1 : _NodeData[node, adjacency_list],
        .
        .
        .
        keyN : _NodeData[node, adjacency_list],
    }
    This way, any GraphNode subclass can be used with this class, due to polymorphism
    """

    def __init__(self) -> None:
        # n is the number of vertices of the graph
        self.n = 0
        # The data is stored inside a dictionary / hashtable
        self._data : Dict = {}

    @classmethod
    def initialize(cls, nodes, key_pairs=[], dir_graph=False):
        # vertices: list(GraphNode)
        # key_pairs: list(node_key_0, node_key_1), adjacent nodes
        # dir_graph: The graph could be constructed as directed

        graph = Graph()
        # Inserts all the nodes
        for node in nodes:
            graph.add(node)

        # Creates the nodes link
        if not dir_graph:
                
            for (node_key0, node_key1) in key_pairs:
                graph.link(node_key0, node_key1)
        else:
            for (node_key0, node_key1) in key_pairs:
                graph.link_dir(node_key0, node_key1)
        return graph
    
    def __getitem__(self, node):
        """Returns the node that has the given key"""
        return self._data[self._get_key(node)].node
    
    def __len__(self):
        return self.n

    @property
    def nodes(self):
        """
        Returns the nodes generator
        """
        for key in self._data:
            yield self._data[key].node

    
    def add(self, node):    
        """
        Adds the node for the first time to the graph
        """
        self.n += 1
        # If the node isn't subclass of GraphNode, then creates one
        if not issubclass(type(node), GraphNode):
            node = GraphNode(node)

        # Adds the new node to data
        if node.key in self._data:
            raise Exception(f"Node: {node.key} already added")
        
        # Initializes the adjacency list
        self._data[node.key] = _NodeData(node)

    def link(self, node0, node1):
        """
        Links two nodes, as in a SimpleGraph
        """
        self.link_dir(node0, node1)
        self.link_dir(node1, node0)

    def link_dir(self, node0, node1):
        """
        Creates one edge, as in a DirGraph
        """
        node0_data = self._data[self._get_key(node0)]
        node1_data = self._data[self._get_key(node1)]
        node0_data.adjacent.append(node1_data)

    def remove_dir(self, node0, node1):
        """
        Creates one edge, as in a DirGraph
        """
        node0_data = self._data[self._get_key(node0)]
        node1_data = self._data[self._get_key(node1)]
        node0_data.adjacent.remove(node1_data)

    def get_adjacent(self, node):
        """
        Returns the adjacency generator of a node
        """
        # Returns the adjacency nodes, as a generator
        n = self._data[self._get_key(node)]
        for adjacent_node_data in n.adjacent:
            yield adjacent_node_data.node

    def _get_key(self, node):
        # Returns the key of the node, even if it already is the key
        if not issubclass(type(node), GraphNode):
            return node
        return node.key