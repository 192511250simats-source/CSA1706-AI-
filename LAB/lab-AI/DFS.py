Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # DFS Algorithm
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
... visited = set()
... 
... def dfs(node):
...     if node not in visited:
...         print(node, end=" ")
...         visited.add(node)
... 
...         for next_node in graph[node]:
...             dfs(next_node)
... 
... print("DFS Traversal:")
