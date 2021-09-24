"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
from typing import TypeVar

Node = TypeVar("Node")


class Solution:
    def flatten(self, head: Node) -> Node:
        if not head:
            return None

        head, tail = self._flatten(head)
        return head

    def _flatten(self, head: Node) -> tuple[Node, Node]:
        cur = head
        tail = head
        while cur:
            tail = cur
            nxt = cur.next
            if cur.child:
                sub_head, sub_tail = self._flatten(cur.child)
                # dealing with sub-head
                cur.next = sub_head
                sub_head.prev = cur
                # dealing with sub-tail
                sub_tail.next = nxt
                if nxt:
                    nxt.prev = sub_tail
                else:
                    tail = sub_tail
                # rm child
                cur.child = None
            cur = nxt
        return head, tail
