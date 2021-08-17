from utils import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]