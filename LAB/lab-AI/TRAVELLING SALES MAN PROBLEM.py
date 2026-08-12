Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Travelling Salesman Problem
... 
... from itertools import permutations
... 
... cities = ['A', 'B', 'C', 'D']
... 
... distance = {
...     'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
...     'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
...     'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
...     'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
... }
... 
... start = 'A'
... min_distance = float('inf')
... best_route = None
... 
... for route in permutations(cities[1:]):
...     path = (start,) + route + (start,)
...     total = 0
... 
...     for i in range(len(path) - 1):
...         total += distance[path[i]][path[i + 1]]
... 
...     if total < min_distance:
...         min_distance = total
...         best_route = path
... 
... print("Best Route:", best_route)
