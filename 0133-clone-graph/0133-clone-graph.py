"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, []) # make a copy the current node

        while q:
            current = q.popleft()

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    # make a copy of this node
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                clone_current = visited[current] # accesses the current clone
                cloned_neighbor = visited[neighbor] # accesses the neighbors of the original
                clone_current.neighbors.append(cloned_neighbor) # add the cloned node type as a node
        
        return visited[node]
        


