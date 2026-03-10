# Graph: DS used to represent relationships between things
# Graphs can be directed or undirected
# Graphs can be weighted or unweighted

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B']
}

# Adjacency Matrix
graph = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 0],  # C
    [0, 1, 0, 0]   # D
]

#graph[i][j] == 1 means there is an edge from node i to node j, while graph[i][j] == 0 means there is no edge.

#1. BFS(Breadth First Search): Explore all neighbors at the present depth before moving on to the nodes at the next depth level. #uses queue
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)  # Process the node
            visited.add(node)
            
            for neighbor in graph[node]:
                queue.append(neighbor)

#2. DFS(Depth First Search): Explore as far as possible along each branch before backtracking. #uses stack
def dfs(graph, start, visited=None):
    if node not in visited:
        print(node)  # Process the node
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)