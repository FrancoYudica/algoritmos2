"""
Dado un grafo conexo y no dirigido, representado por una lista de adyacencia,
proponer un algoritmo que devuelva True si existe en G un nodo que al 
eliminarlo aumenta el numero de componentes conexas dentro de grafo.
Devolver False en caso de que no exista ese nodo
"""

def connected_components(graph):
    # Time complexity, O(|V| + |E|)
    # Counts the amount of connected components
    # traversing the graph with DFS

    def _visit(node, visited, graph):
        if node in visited:
            return
        
        visited.add(node)

        for adyacent in graph[node]:
            _visit(adyacent, visited, graph)

    count = 0
    visited = set()
    for node in graph.keys():

        if node not in visited:
            count += 1
            _visit(node, visited, graph)

    return count



def can_increase_connected_count(graph):
    """
    The algorithm has a time complexity of O((V + E)^2)
    """
    connected_count = connected_components(graph)
    keys = list(graph.keys())

    # Loops through all the nodes
    for node in keys:
        
        # Removes the node from the graph
        adyacent_nodes = graph[node]

        for adyacent in graph[node]:
            graph[adyacent].remove(node)

        del graph[node]

        # If the amount of components increased -> True
        if connected_components(graph) > connected_count:
            return True
        
        # Adds the node back
        graph[node] = []
        for adyacent in adyacent_nodes:
            graph[node].append(adyacent)
            graph[adyacent].append(node)

    return False


def find_articulation_nodes(graph):
    # O(V + A) complexity
    def _dfs_visit(graph, node, visited, parent, ap, time, low_adyacent, current_time):

        visited[node] = True
        time[node] = current_time
        low_adyacent[node] = current_time
        current_time += 1
        disconnected_children = 0

        for adyacent in graph[node]:

            if adyacent == parent[node]:
                continue

            if visited[adyacent] == False:
                
                disconnected_children += 1

                # Visited
                parent[adyacent] = node
                _dfs_visit(graph, adyacent, visited, parent, ap, time, low_adyacent, current_time)
                
                # If the subtree rooted with adyacent has a connection with ancestors of node
                # copies the ancestor connection
                low_adyacent[node] = min(low_adyacent[node], low_adyacent[adyacent])

                # Inner node
                if parent[node] != -1:

                    # When the sub-graph has no connection with ancestors
                    # we can remove node, increasing the connected components
                    if low_adyacent[adyacent] >= time[node]:
                        ap[node] = True

                # Root node, has no parent
                else:

                    # If we have 2 disconeccted sub-graph, we can remove node
                    # increasing the connected components
                    if disconnected_children >= 2:
                        ap[node] = True

            else:
                # The node could be connected to an ancestor
                # in this case, updates the low_time
                low_adyacent[node] = min(time[adyacent], low_adyacent[node])
                    

    # Assumes that the vertices are numbers from 0 to n - 1
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = [None for _ in range(n)]
    low_adyacent = [float("inf") for _ in range(n)]
    ap = [False for _ in range(n)]
    current_time = 0
    for node in graph.keys():
        
        if not visited[node]:
            _dfs_visit(graph, node, visited, parent, ap, time, low_adyacent, current_time)
    

    print(ap)


def add_edge(graph, node0, node1):

    if node0 not in graph:
        graph[node0] = []

    if node1 not in graph:
        graph[node1] = []

    graph[node0].append(node1)
    graph[node1].append(node0)


if __name__ == "__main__":


    graph = {}
    add_edge(graph, 0, 1)
    add_edge(graph, 1, 2)
    add_edge(graph, 2, 0)
    add_edge(graph, 1, 3)
    add_edge(graph, 1, 4)
    add_edge(graph, 1, 6)
    add_edge(graph, 3, 5)
    add_edge(graph, 4, 5)

    find_articulation_nodes(graph)