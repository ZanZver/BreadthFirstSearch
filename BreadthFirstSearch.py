from collections import deque
import timeit

class Node:
    def __init__(self, value, children=None):
        # a leaf node has an empty list of children
        if children is None:
            children = []
        self.value = value
        self.children = children

root = Node(1, [
    Node(2, [
        Node(3, [
            Node(4),
            Node(5)
        ]),
        Node(6)
    ]),
    Node(7, [
        Node(8, [
            Node(9)
        ])
    ]),
    Node(10)
])

def breadth_first_search(root_node, target):
    # create a queue of nodes to visit
    nodes_to_visit = deque([root_node])
    
    while nodes_to_visit:
        # visit the next node
        node = nodes_to_visit.popleft()
        
        if node.value == target:
            # found it!
            return node
        
        # make sure we visit the child nodes
        for child in node.children:
            nodes_to_visit.append(child)
    
    # no more nodes to visit, target wasn't found
    return None

start_time = timeit.default_timer()
#print(breadth_first_search(root,8))
breadth_first_search(root,8)
elapsed = timeit.default_timer() - start_time
print("Print breadth first: ")
print(elapsed)