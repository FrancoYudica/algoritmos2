
def initialize_adj_matrix(node_count, init_val=0):
    return [[init_val for _ in range(node_count)] for _ in range(node_count)]


def add_edge_matrix(graph: list, e1, e2):
    graph[e1][e2] = 1
    graph[e2][e1] = 1


def _dfs_bridge(graph, node, visited, discovery_time, low_adjacent_time, parent, time: int, bridges):

    visited[node] = True
    discovery_time[node] = time
    low_adjacent_time[node] = time
    time += 1

    # Iterates through all the row
    for adyacent, is_adyacent in enumerate(graph[node]):
        
        # Only care about adyacent nodes
        if not is_adyacent:
            continue

        if adyacent == parent[node]:
            continue

        if not visited[adyacent]:
            parent[adyacent] = node
            _dfs_bridge(graph, adyacent, visited, discovery_time, low_adjacent_time, parent, time, bridges)

            # Propagates the lower adyacent time
            low_adjacent_time[node] = min(low_adjacent_time[node], low_adjacent_time[adyacent])
            
            if low_adjacent_time[adyacent] > discovery_time[node]:
                # The tree rooted with adyacent has no regression edge to
                # node parents
                bridges.append((node, adyacent))
        else:
            low_adjacent_time[node] = min(low_adjacent_time[node], discovery_time[adyacent])

def get_bridges(graph: dict):

    """
    Uses Tarjan's theorem, therefore the time complexity is O(V + E)
    """

    node_count = len(graph)
    visited = [False] * node_count
    discovery_time = [None] * node_count
    parent = [None] * node_count
    low_adjacent_time = [None] * node_count
    bridges = []
    time = 0

    for node in range(node_count):
        if not visited[node]:
            _dfs_bridge(graph, node, visited, discovery_time, low_adjacent_time, parent, time, bridges)

    return bridges

if __name__ == "__main__":
    graph1 = initialize_adj_matrix(5)
    add_edge_matrix(graph1, 0, 1)
    add_edge_matrix(graph1, 0, 2)
    add_edge_matrix(graph1, 0, 3)
    add_edge_matrix(graph1, 1, 2)
    add_edge_matrix(graph1, 3, 4)
    bridges1 = get_bridges(graph1)
    print(bridges1)