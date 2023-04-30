"""
Simple implementation of the algorithms using Dict[List[Node]]
"""


def bfs(graph, root):


    tree = {}
    queue = [root]
    visited_keys = set()
    visited_keys.add(root)

    while len(queue):

        key = queue.pop(0)
        tree[key] = list()
        for adjacent_key in graph[key]:

            if adjacent_key in visited_keys:
                continue

            visited_keys.add(adjacent_key)
            tree[key].append(adjacent_key)
            queue.append(adjacent_key)

    return tree


def dfs(graph : dict):


    def _visit(graph, tree, key, visited):

        if key in visited:
            return
        
        visited.add(key)
        tree[key] = list()

        for adjacent_key in graph[key]:

            if adjacent_key in visited:
                continue
                
            tree[key].append(adjacent_key)
            _visit(graph, tree, adjacent_key, visited)
            

    tree = {}
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