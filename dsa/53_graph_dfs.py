def dfs_recursive(graph, node, visited=None, path=None):
    # Initialize collections on the first call
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Mark the current node as visited and add to our path
    visited.add(node)
    path.append(node)

    # Explore all unvisited neighbors
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, path)

    return path


# We use an Adjacency List to represent the graph.
# Graph Structure:
# 0 --- 1 --- 2
# |     |
# 3 --- 4
adjacency_list = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1],
    3: [0, 4],
    4: [1, 3]
}

print("Available nodes: 0, 1, 2, 3, 4")
start_node = int(input("Enter starting node: "))

if start_node in adjacency_list:
    traversal_path = dfs_recursive(adjacency_list, start_node)
    print(f"DFS Traversal path: {' -> '.join(map(str, traversal_path))}")
else:
    print("Invalid node.")