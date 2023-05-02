"""
Simple implementation of the algorithms using Dict[List[Node]]
"""


def bfs(graph, root):


    tree = {}
    for node in graph.keys():
        tree[node] = []

    queue = [root]
    visited_keys = set()
    visited_keys.add(root)

    while len(queue):

        key = queue.pop(0)
        for adjacent_key in graph[key]:

            if adjacent_key in visited_keys:
                continue

            visited_keys.add(adjacent_key)
            tree[key].append(adjacent_key)
            tree[adjacent_key].append(key)
            
            queue.append(adjacent_key)

    return tree


def dfs(graph : dict):


    def _visit(graph, tree, key, visited):

        if key in visited:
            return
        
        visited.add(key)

        for adjacent_key in graph[key]:
            
            # Already visited
            if adjacent_key in visited:
                continue

            # Links the nodes in the adjacency list 
            tree[key].append(adjacent_key)
            tree[adjacent_key].append(key)
            _visit(graph, tree, adjacent_key, visited)
            

    # Initializes the tree
    tree = {}

    for node in graph.keys():
        tree[node] = []

    visited = set()

    for key in graph.keys():
        _visit(graph, tree, key, visited)

    return tree

if __name__ == "__main__":

    graph = {
        1 : [5],
        2 : [5, 4],
        3 : [4],
        4 : [5, 3],
        5 : [1, 2, 4]
    }
    print(bfs(graph, 1))