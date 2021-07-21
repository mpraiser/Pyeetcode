from typing import TypeVar


ListNode = TypeVar("ListNode")


# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         n1 = headA
#         n2 = headB
#         r1 = True
#         r2 = True
#         while n1 and n2:
#             if n1 == n2:
#                 return n1
#             if r1 and (not n1.next):
#                 n1 = headB
#                 r1 = False
#             else:
#                 n1 = n1.next
#             if r2 and (not n2.next):
#                 n2 = headA
#                 r2 = False
#             else:
#                 n2 = n2.next
#         return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        n1 = headA
        n2 = headB
        while n1 != n2:
            n1 = headB if n1 is None else n1.next
            n2 = headA if n2 is None else n2.next
        return n1
