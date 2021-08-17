from utils import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last_node = None
        node = head
        while node:
            next_node = node.next
            node.next = last_node
            last_node = node
            node = next_node
        return last_node
