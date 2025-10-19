from collections import deque

# Definition for a Node
class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []

# Clone the graph
def cloneGraph(node):
    if not node:
        return None

    # Map to hold original nodes as keys and their clones as values
    mp = {}

    # Initialize BFS queue
    q = deque([node])

    # Clone the starting node
    mp[node] = Node(node.val)

    while q:
        current = q.popleft()

        for neighbor in current.neighbors:
            
            # If neighbor not cloned yet
            if neighbor not in mp:
                mp[neighbor] = Node(neighbor.val)
                q.append(neighbor)

            # Link clone of neighbor to the clone of the current node
            mp[current].neighbors.append(mp[neighbor])

    return mp[node]

# Build graph
def buildGraph():
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)

    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2, node4]
    node4.neighbors = [node3]

    return node1

# Compare two graphs structurally and by values
def compareGraphs(n1, n2, visited):
    
    if not n1 or not n2:
        return n1 == n2
        
    if n1.val != n2.val or n1 is n2:
        return False

    visited[n1] = n2

    if len(n1.neighbors) != len(n2.neighbors):
        return False

    for i in range(len(n1.neighbors)):
        neighbor1 = n1.neighbors[i]
        neighbor2 = n2.neighbors[i]

        if neighbor1 in visited:
            if visited[neighbor1] != neighbor2:
                return False
                
        else:
            if not compareGraphs(neighbor1, neighbor2, visited):
                return False

    return True

# Driver
if __name__ == "__main__":
    original = buildGraph()
    cloned = cloneGraph(original)
    result = compareGraphs(original, cloned, {})
    print("true" if result else "false")
