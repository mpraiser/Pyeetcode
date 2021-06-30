# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        new_head = stack.pop()
        node = new_head
        while len(stack) > 0:
            node.next = stack.pop()
            node = node.next
        node.next = None

        return new_head