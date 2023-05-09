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
    
    # UNCOMPLETED
    # Edges is a directed graph
    edges = {node : set() for node in graph.keys()}

    # Builds the directed graph
    for node in graph.keys():

        for ady, weight in graph[node]:

            if (node, weight) in edges[ady]:
                continue

            edges[node].add((ady, weight))

    edges_count = sum([len(edges[node]) for node in edges.keys()])        
    heap = Heap(edges_count)

    # Inserts the edges in the heap
    for node in edges.keys():
        for ady, weight in edges[node]:
            heap.add((node, ady), weight)


    # At this stage, heap contains unique edges.
    # contains (u, v) and not (u, v), (v, u)
    parent = {}
    while len(heap):
        (u, v), weight = heap.pop()

        if u not in parent:
            parent[u] = (v, weight)

        elif parent[u][1] > weight:
            parent[u] = (v, weight)

        elif v not in parent:
            parent[v] = (u, weight)

        elif parent[v][1] > weight:
            parent[v] = (u, weight)

    result_graph = {}
    total_weight = 0
    for node in parent.keys():
        ady, weight = parent[node]
        weight_insert_double(result_graph, node, ady, weight)

        total_weight += weight

    print(f"Weight: {total_weight}")
    return result_graph

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

    mst = kruskal(graph) # The total weight should be 37
    print(mst)