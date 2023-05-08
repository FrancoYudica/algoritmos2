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


if __name__ == "__main__":

    graph = {
        1 : [2, 4, 5],
        2 : [1],
        3 : [6, 7],
        4 : [1, 5],
        5 : [1, 4],
        6 : [3, 7],
        7 : [3, 6]
    }

    print(can_increase_connected_count(graph))

