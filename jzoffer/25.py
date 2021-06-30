# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        node = head
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    node = node.next
                    l1 = l1.next
                else:
                    node.next = l2
                    node = node.next
                    l2 = l2.next
            elif l1:
                node.next = l1
                node = node.next
                l1 = l1.next
            elif l2:
                node.next = l2
                node = node.next
                l2 = l2.next
        return head