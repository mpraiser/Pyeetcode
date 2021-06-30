from utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(0, None)
        node = sentinel
        carry = 0
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            carry = s // 10
            node.next = ListNode(s % 10, None)
            node = node.next
        return sentinel.next


a = ListNode.parse([9, 9, 9, 9, 9, 9, 9])
b = ListNode.parse([9, 9, 9, 9])
ans = Solution().addTwoNumbers(a, b)
print(ans.serialize())
