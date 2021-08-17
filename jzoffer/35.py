from utils import ListNode as Node
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
        if not head:
            return None

        cache = {}

        def copy(raw):
            if raw in cache:
                return cache[raw]
            new = Node(raw.val)
            cache[raw] = new
            if raw.next:
                new.next = copy(raw.next)
            if raw.random:
                new.random = copy(raw.random)
            return new

        return copy(head)
