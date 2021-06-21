"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        cache = {}
        def copy_node(src):
            if src is None:
                return src
            if src in cache:
                return cache[src]
            else: 
                dst = Node(src.val, None, None)
                cache[src] = dst
                if src.next:
                    dst.next = copy_node(src.next)
                if src.random:
                    dst.random = copy_node(src.random)
                return dst
        return copy_node(head)


# 似乎这正是图的DFS？