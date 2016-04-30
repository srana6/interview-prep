from collections import deque

# Comment class for submission
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        clone = UndirectedGraphNode(node.label)
        queue = deque([node])
        visited = {node: clone}
        
        while queue:
            next = queue.popleft()
            for adj in next.neighbors:
                if adj not in visited:
                    adjClone = UndirectedGraphNode(adj.label)
                    visited[next].neighbors.append(adjClone)
                    visited[adj] = adjClone
                    queue.append(adj)
                else:
                    visited[next].neighbors.append(visited[adj])
        return clone



n0 = UndirectedGraphNode(0)
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)

n0.neighbors = [n1, n2]
n1.neighbors = [n2]
n2.neighbors = [n2]

sol = Solution()
sol.cloneGraph(n0)