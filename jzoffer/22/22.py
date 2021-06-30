class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        counter = 0  # distance from this node to the last one
        node = head
        target = node
        while node:
            if counter >= k:
                target = target.next
            else:
                counter += 1
            node = node.next
        return target