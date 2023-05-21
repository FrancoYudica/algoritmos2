from min_heap import Heap


def weight_insert(graph, node, ady_node, weight):
    
    # Adds both nodes to the graph
    if node not in graph:
        graph[node] = []

    if ady_node not in graph:
        graph[ady_node] = []

    # But the directed edge is node -> ady_node
    graph[node].append((ady_node, weight))


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.d = float("inf")
        self.parent = None


def relax(node_u, node_v, weight):

    if node_v.d > node_u.d + weight:
        node_v.d = node_u.d + weight
        node_v.parent = node_u
        return True
    
    return False


def dijkstra(graph, start_key, end_key):

    edges_count = sum(len(graph[node_key]) for node_key in graph.keys())

    # Stores the Node instances
    nodes = {}          

    # Heap used to get the min distance item
    heap = Heap(edges_count)
    for node_key in graph.keys():
        nodes[node_key] = Node(node_key)
        heap.add(node_key, float("inf"))

    visited_keys = set()

    # Sets the d value of the starting node to 0
    # this way the heap pops the start first
    heap.update_key(start_key, 0)
    nodes[start_key].d = 0

    while len(heap):

        (node_key, d) = heap.pop()

        # Shortest path already found
        if node_key == end_key:
            break

        visited_keys.add(node_key)

        # Gets the node, containing d, and parent data
        node = nodes[node_key]

        for ady, weight in graph[node_key]:

            if ady not in visited_keys:

                ady_node = nodes[ady]

                # Relax the adyacent
                modified = relax(node, ady_node, weight)

                # Only if the relax call modified the value
                if modified:
                    heap.update_key(ady, ady_node.d)

    end_node = nodes[end_key]

    # No path, unreachable from start_key
    if end_node.parent is None:
        return None

    # Traverses the path backwards, using the parent attribute 
    path = []
    parent = end_node
    while parent is not None:
        path.append(parent.key)
        parent = parent.parent

    return path

if __name__ == "__main__":

    graph = {}

    # Connected group
    weight_insert(graph, "s", "t", 10)
    weight_insert(graph, "s", "y", 5)
    weight_insert(graph, "t", "y", 2)
    weight_insert(graph, "t", "x", 1)
    weight_insert(graph, "y", "t", 3)
    weight_insert(graph, "y", "z", 2)
    weight_insert(graph, "y", "x", 9)
    weight_insert(graph, "z", "s", 7)
    weight_insert(graph, "z", "x", 6)
    weight_insert(graph, "x", "z", 4)

    # unconnected group
    weight_insert(graph, "m", "n", 4)

    print("Path from 's' to 'x':", dijkstra(graph, "s", "x"))
    print("Path from 's' to 'b':", dijkstra(graph, "s", "n"))