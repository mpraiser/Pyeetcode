from typing import List


def reversed_nodes(head: ListNode) -> List:
    node = head
    r = []
    while node:
        r.append(node)
        node = node.next
    return list(reversed(r))


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        reversed_a = reversed_nodes(headA)
        reversed_b = reversed_nodes(headB)

        last_intersect = None
        for i, a in enumerate(reversed_a):
            if i < len(reversed_b) and reversed_a[i] == reversed_b[i]:
                last_intersect = a
            else:
                break
        return last_intersect