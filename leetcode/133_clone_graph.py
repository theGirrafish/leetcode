# https://leetcode.com/problems/clone-graph/

from typing import Optional


class GraphNode:
    def __init__(self, val: int = 0, neighbors: list['GraphNode'] = None):
        self.val = val
        self.neighbors = neighbors or []


class Solution:
    def cloneGraph(self, node: Optional[GraphNode]) -> Optional[GraphNode]:
        if not node:
            return None

        seen = {}
        def traverse(n: GraphNode) -> GraphNode:
            new_node = GraphNode(n.val)
            seen[new_node.val] = new_node

            for neighbor in n.neighbors:
                if neighbor.val in seen:
                    new_node.neighbors.append(seen[neighbor.val])
                else:
                    new_neighbor = traverse(neighbor)
                    new_node.neighbors.append(new_neighbor)
            return new_node

        return traverse(node)
