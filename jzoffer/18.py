class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        node = head
        node_last = None
        while node:
            if node.val == val:
                if node_last:
                    node_last.next = node.next
                else:
                    head = node.next
            node_last = node
            node = node.next
        return head