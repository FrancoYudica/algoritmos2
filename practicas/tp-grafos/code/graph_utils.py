from graph import Graph


def exists_path(graph, node0, node1):
    """Returns if there is a path that connects the vertices"""
    # Uses a similar algorithm to Breadth-First-Search

    starting_node = graph[node0]
    end_node = graph[node1]
    
    queue = [starting_node]
    traversed_keys = set()
    
    while len(queue):
        node = queue.pop(0)
        if node.key == end_node.key:
            return True
        # Stores the traversed vertex in a dictionary
        traversed_keys.add(node.key)
        # Loops throught all the adjacent vertices and adds them to the queue
        for adjacent_node in graph.get_adjacent(node):
            # If the vertex wasn't added to the queue, adds
            if adjacent_node.key not in traversed_keys:
                queue.append(adjacent_node)
                
    return False


def breadth_first_search_tree(graph, root):
    """
    Returns a Tree
    """

    root_node = graph[root]

    tree_graph = Graph()
    tree_graph.add(root_node)

    # Stores the keys of the traversed nodes
    traversed_keys = set()
    traversed_keys.add(root_node.key)
    queue = [root_node]
    while len(queue):
        node = queue.pop(0)

        for adjacent_node in graph.get_adjacent(node):

            if adjacent_node.key not in traversed_keys:
                queue.append(adjacent_node)

                # Adds the node and links with it's parent
                tree_graph.add(adjacent_node)
                tree_graph.link(node, adjacent_node)
                traversed_keys.add(adjacent_node.key)

    return tree_graph


def depth_first_search_tree(graph : Graph, root):

    tree_graph = Graph()
    root_node = graph[root]

    visited_keys = set()

    time = 0

    # Visits the root
    dfs_visit(graph, tree_graph, root_node, time, visited_keys)

    # Visits the other nodes
    for node in graph.nodes:

        # Visits the node
        if node.key not in visited_keys:
            dfs_visit(graph, tree_graph, node, time, visited_keys)

    return tree_graph

def dfs_visit(graph, tree_graph, node, time, visited_keys):

    tree_graph.add(node)
    visited_keys.add(node.key)

    time += 1
    node.t0 = time

    for adjacent_node in graph.get_adjacent(node):
        
        # Backwards edge
        if adjacent_node.key not in visited_keys:
            dfs_visit(graph, tree_graph, adjacent_node, time, visited_keys)
            tree_graph.link(node, adjacent_node)

    time += 1
    node.t1 = time

def is_connected(graph):
    """
    Uses a DFS approach. With DFS we can count the amount of 
    connected components in the main for loop. If the counter is
    greater than 1, it means it's not connected
    """
    def _visit_node(graph, node, visited_keys):
        # Recursive function, used to visit all the adyacent nodes
        if node.key in visited_keys:
            return
        
        visited_keys.add(node.key)

        for adjacent_node in graph.get_adjacent(node):
            _visit_node(graph, adjacent_node, visited_keys)


    visited_keys = set()
    components = 0
    for node in graph.nodes:
        
        if node.key not in visited_keys:
            
            # More than one connected component
            if components == 1:
                return False

            components += 1
            _visit_node(graph, node, visited_keys)

    return True



def is_tree(graph: Graph):
    """
    Uses a DFS approach.
    Cycle detection: we can check if any of the adjacent nodes
        have already been visited, and if it's not an immediate parent, it means
        we found a regession edge -> cycles -> not tree
    Connected: As in the is_connected(graph) implementation, counts the amount
        of connected components, and in a tree it should be just one 
    """

    def visit_is_tree_node(graph, node, visited_keys, immediate_parent):

        # Node already visited
        if node.key in visited_keys:
            return True
        
        # Visited for the first time
        visited_keys.add(node.key)
        
        # Loops throught all the adjacent nodes
        for adjacent_node in graph.get_adjacent(node):
            
            if adjacent_node.key in visited_keys:

                # If the node is already visited and it's not it's parent
                # it means we found a regression edge, making a cycle, then it's not a tree
                if adjacent_node != immediate_parent: return False
            
            tree = visit_is_tree_node(graph, adjacent_node, visited_keys, node)
            if not tree: return False
                
        return True

    # Uses hash table
    visited_keys = set()
    components = 0

    for node in graph.nodes:
        
        if node.key not in visited_keys:

            # Not connected
            if components == 1:
                return False
            
            components += 1
            tree = visit_is_tree_node(graph, node, visited_keys, None)

        if not tree: 
            return False

    return True


def is_complete(graph):
    """
    A complete graph is an undirected graph in which every
    pair of distinct vertices is connected by a unique edge
    This implementation assumes that the graph is simple
    """
    for node in graph.nodes:
        
        if len(graph) - 1 != len(list(graph.get_adjacent(node))):
            return False

    return True


def convert_tree(graph):
    """
    Returtns the list of edges that when removed, make the graph a tree
    Note it's almost the same algorithm as is_tree
    """

    def _visit(graph, node, visited_keys, remove_edges, immnediate_parent):

        if node.key in visited_keys:
            return
        
        visited_keys.add(node.key)

        for adjacent_node in graph.get_adjacent(node):

            if adjacent_node.key in visited_keys:
                
                if adjacent_node != immnediate_parent:
                    # Regression edge
                    remove_edges.append((node, adjacent_node))

            _visit(graph, adjacent_node, visited_keys, remove_edges, node)

    remove_edges = []
    visited_keys = set()

    for node in graph.nodes:
        _visit(graph, node, visited_keys, remove_edges, None)


    return remove_edges


def connections_count(graph):

    """
    Returns the amount of connected components
    Uses DFS, and counts the component in the main loop
    """
    def _visit(graph, node, visited_keys):
        if node.key in visited_keys:
            return
        
        visited_keys.add(node.key)

        for adjacent_node in graph.get_adjacent(node):
            _visit(graph, adjacent_node, visited_keys)

    visited_keys = set()    
    connections = 0

    for node in graph.nodes:

        if node.key not in visited_keys:
            connections += 1
            _visit(graph, node, visited_keys)

    return connections


def best_road(graph, start, end):
    """
    Returns a list of the edges that make the shortest path
    Uses a BFS approach.
    Stores all the posible paths inside a list, for each iteration,
    a new path is added to paths, until we find the end
    """

    start_node = graph[start]
    end_node = graph[end]

    if start_node == end_node:
        return [start_node]

    visited_keys = set()
    visited_keys.add(start_node.key)

    paths = [[start_node]]
    path_index = 0

    while path_index < len(paths):

        path = paths[path_index]
        last_node = path[-1]

        for adjacent_node in graph.get_adjacent(last_node):
            
            # Already visited
            if adjacent_node.key in visited_keys:
                continue
            
            # Path found
            if adjacent_node == end_node:
                return path + [adjacent_node]
            
            visited_keys.add(last_node.key)
            paths.append(path + [adjacent_node])

        path_index += 1

    return []


def is_bipartite(graph):

    # A graph G=(V, E) is bipartite when for each edge
    # (u, v) of E, u and v belong to different sets

    def _visit_bipartite(graph, node, group_0, group_1, parent_group_0):
        
        # 1) When the node is already added
        if node.key in group_0:

            # If the node is in the same group as the parent
            if parent_group_0:
                return False
            
            return True

        if node.key in group_1:

            # If the node is in the same group as the parent
            if not parent_group_0:
                return False
            
            return True
        
        # 2) Adds the node to it's corresponding list (different to parent)
        if parent_group_0:
            group_1.add(node.key)

        else:
            group_0.add(node.key)
        
        for adjacent_node in graph.get_adjacent(node):
            bipartite = _visit_bipartite(graph, adjacent_node, group_0, group_1, not parent_group_0)
            if not bipartite:
                return False
            
        return True


    group_0 = set()
    group_1 = set()

    for node in graph.nodes:

        if node.key in group_0 or node.key in group_1:
            continue
        bipartite = _visit_bipartite(graph, node, group_0, group_1, False)
        if not bipartite:
            return False
        
    return True