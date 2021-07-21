from utils.listnode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cache = set()
        n1 = headA
        while n1:
            cache.add(n1)
            n1 = n1.next
        n2 = headB
        while n2:
            if n2 in cache:
                return n2
            n2 = n2.next
        return None
