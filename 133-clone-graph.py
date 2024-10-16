# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        refTable = {}

        def clone(node):
            if node in refTable:
                return refTable[node]
            
            copy = Node(node.val)
            refTable[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy
        
        return clone(node) if node else None
            

nodes = []
for i in range(4):
    nodes.append(Node(i))

nodes[0].neighbors = [nodes[1], nodes[3]]
nodes[1].neighbors = [nodes[0], nodes[2]]
nodes[2].neighbors = [nodes[1], nodes[3]]
nodes[3].neighbors = [nodes[0], nodes[2]]

s = Solution()

result = s.cloneGraph(nodes[0])

