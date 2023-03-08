from collections import defaultdict
from typing import List, Dict, Set

class Graph:
    def __init__(self) -> None:
        self.graph = {}
        
    def build(self, v1: int, v2: int) -> None:
        if str(v1) not in self.graph:
            self.graph[str(v1)] = [v2]
        else:
            self.graph[str(v1)].append(v2)

    def dfs(self, node: int, visited: Set) -> None: 
        if node in visited:
            return
        print(node)
        visited.add(node)
        if str(node) in self.graph:
            for neighbor in self.graph[str(node)]:
                self.dfs(neighbor, visited)

graph = Graph()
# nodes = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 4), (3, 5), (3, 6), (4, 7), (4, 5), (5, 2)]
nodes = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
for i in range(len(nodes)):
    graph.build(nodes[i][0], nodes[i][1])
visited = set()
graph.dfs(3, visited)




        