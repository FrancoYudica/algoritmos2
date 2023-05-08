from min_heap import Heap



def weight_insert(graph, node, ady_node, weight):
    
    if node not in graph:
        graph[node] = []

    graph[node].append((ady_node, weight))

def weight_insert_double(graph, node, ady_node, weight):
    weight_insert(graph, node, ady_node, weight)
    weight_insert(graph, ady_node, node, weight)


def weight_remove(graph, node, ady_node):

    index = -1  
    for i, (ady, weight) in enumerate(graph[node]):
        if ady == ady_node:
            index = i
            break

    if index == -1:
        raise IndexError(f"Unable to find node: {ady_node} in the adyacency list of the node: {node}")

    graph[node].pop(index)


def prim(graph: dict):
    
    new_graph = {}
    first_key = list(graph.keys())[0]
    added = set(first_key)
    total_weight = 0

    while len(added) < len(graph):

        minimum_weight = float("inf")
        minimum_node = None
        node = None

        # Finds the new adyacent node with the least weight
        for added_node in added:
            for (adyacent_key, weight) in graph[added_node]:

                if adyacent_key not in added:
                    if weight < minimum_weight:
                        minimum_node = adyacent_key
                        minimum_weight = weight
                        node = added_node

        if minimum_node is not None:

            # Addds the edge to the graph
            weight_insert_double(new_graph, node, minimum_node, minimum_weight)
            added.add(minimum_node)

            total_weight += minimum_weight

    print(total_weight)
    return new_graph


def prim_optimized(graph: dict):

    heap = Heap(len(graph))
    smaller_weights = {}

    # Initializes the heap and weights as maximum
    for node in graph.keys():
        min_weight = 1e7
        smaller_weights[node] = min_weight
        heap.add(node, min_weight)

    # Updates the first key, so it gets extracted first
    first_key = list(graph.keys())[0]
    heap.update_key(first_key, 0)

    # Holds the parent-child results
    parent = {}

    while len(heap):
        
        # Gets the edge with the smallest weight
        min_key, min_weight = heap.pop()

        for (adyacent_node, weight) in graph[min_key]:
            
            # If it doesn't make a cycle and the weight isn't the smallest
            if adyacent_node in heap and weight < heap.access(adyacent_node):
                parent[adyacent_node] = (min_key, weight)
                
                # Adds to the tree
                heap.update_key(adyacent_node, weight)                

    # Builds the graph, using the parent dict
    result_tree = {}
    total_weight = 0
    for node in parent.keys():
        child, weight = parent[node]
        weight_insert_double(result_tree, node, child, weight)

        total_weight += weight

    print(f"Weight: {total_weight}")

    return result_tree


def kruskal(graph: dict):

    edges = []
    nodes = list(graph.keys())
    edges_set = {}
    for i, node in enumerate(nodes):
        edges_set[node] = i
        for adyacent_key, edge_weight in graph[node]:
            edges.append((node, adyacent_key, edge_weight))

    sorted_edges = sorted(edges, key=lambda e1: e1[2])
    print(sorted_edges)
    print(edges_set)

    new_graph = {}

    while len(new_graph) < len(graph):
        edge = sorted_edges.pop(0)
        node0 = edge[0]
        node1 = edge[1]
        weight = edge[2]

        if edges_set[node0] != edges_set[node1]:
            # Merges the sets
            edges_set[node1] = edges_set[node0]
        


if __name__ == "__main__":

    # Edges are tuples, where for each pair
    # there is the adjacent node and the weight
    graph = {}
    weight_insert_double(graph, "a", "b", 4)
    weight_insert_double(graph, "a", "h", 8)
    weight_insert_double(graph, "b", "c", 8)
    weight_insert_double(graph, "h", "i", 7)
    weight_insert_double(graph, "h", "b", 11)
    weight_insert_double(graph, "h", "g", 1)
    weight_insert_double(graph, "c", "i", 2)
    weight_insert_double(graph, "c", "d", 7)
    weight_insert_double(graph, "c", "f", 4)
    weight_insert_double(graph, "i", "g", 6)
    weight_insert_double(graph, "g", "f", 2)
    weight_insert_double(graph, "d", "e", 9)
    weight_insert_double(graph, "d", "f", 14)
    weight_insert_double(graph, "f", "e", 10)

    mst = prim_optimized(graph) # The total weight should be 37
    print(mst)
