"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        cache = dict()

        def deepcopy_node(node: 'Node') -> 'Node':
            nonlocal cache
            if node in cache:
                return cache[node]
            if node:
                copied = Node(node.val, None, None)
                cache[node] = copied
            if node.next:
                copied.next = deepcopy_node(node.next)
            if node.random:
                copied.random = deepcopy_node(node.random)
            return copied
        
        return deepcopy_node(head)
