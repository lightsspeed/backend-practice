# This is 3.py

# Write a program to implement a depth-first search (DFS) on a graph represented as an adjacency list (e.g., {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}).


def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
dfs(graph, 0, set())  # Output: 0 1 3 2