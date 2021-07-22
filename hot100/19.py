from utils import ListNode
from collections import deque


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        this method takes O(N) space complexity
        """
        dq = deque()
        node = head
        while node:
            dq.append(node)
            node = node.next
        if n == len(dq):
            if len(dq) == 1:
                return None
            else:
                return dq[1]
        elif n == 1:
            dq[-2].next = None
            return dq[0]
        else:
            dq[-n-1].next = dq[-n+1]
            return dq[0]


# ans = Solution().removeNthFromEnd(ListNode.parse([1,2,3,4,5]), 2)
ans = Solution().removeNthFromEnd(ListNode.parse([1, 2]), 1)
print(ans)
print(ans.serialize())
