Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # BFS Algorithm
... 
... graph = {
...     'A': ['B', 'C'],
...     'B': ['D', 'E'],
...     'C': ['F'],
...     'D': [],
...     'E': [],
...     'F': []
... }
... 
... def bfs(start):
...     visited = []
...     queue = [start]
... 
...     while queue:
...         node = queue.pop(0)
... 
...         if node not in visited:
...             print(node, end=" ")
...             visited.append(node)
...             queue.extend(graph[node])
... 
... print("BFS Traversal:")
