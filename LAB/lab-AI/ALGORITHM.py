Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# A* Algorithm

import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('E', 2)],
    'D': [('G', 2)],
    'E': [('G', 3)],
...     'G': []
... }
... 
... heuristic = {
...     'A': 5,
...     'B': 4,
...     'C': 3,
...     'D': 2,
...     'E': 2,
...     'G': 0
... }
... 
... def astar(start, goal):
...     queue = [(heuristic[start], 0, start, [start])]
...     visited = set()
... 
...     while queue:
...         f, cost, node, path = heapq.heappop(queue)
... 
...         if node == goal:
...             return path, cost
... 
...         if node in visited:
...             continue
... 
...         visited.add(node)
... 
...         for next_node, edge_cost in graph[node]:
...             new_cost = cost + edge_cost
...             new_f = new_cost + heuristic[next_node]
... 
...             heapq.heappush(
...                 queue,
...                 (new_f, new_cost, next_node, path + [next_node])
...             )
... 
... path, cost = astar('A', 'G')
... 
... print("Shortest Path:", path)
