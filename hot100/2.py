from utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return None
        head = ListNode(0, None)
        node = head
        last_node = None
        carry = 0
        while l1 or l2 or carry != 0:
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            node.val += carry
            next_carry = node.val // 10
            node.val = node.val % 10
            if last_node:
                last_node.next = node
            # next iter
            last_node = node
            node = ListNode(0, None)
            carry = next_carry
        return head


a = ListNode.parse([9, 9, 9, 9, 9, 9, 9])
b = ListNode.parse([9, 9, 9, 9])
ans = Solution().addTwoNumbers(a, b)
print(ans)
