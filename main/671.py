from utils import TreeNode

import heapq
from typing import Tuple


class Solution:
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def two_min(node: TreeNode) -> Tuple[int, int]:
            buf = []
            heapq.heapify(buf)
            heapq.heappush(buf, node.val)
            if node.left:
                a, b = two_min(node.left)
                if a >= 0 and a not in buf:
                    heapq.heappush(buf, a)
                if b >= 0 and b not in buf:
                    heapq.heappush(buf, b)
            if node.right:
                a, b = two_min(node.right)
                if a >= 0 and a not in buf:
                    heapq.heappush(buf, a)
                if b >= 0 and b not in buf:
                    heapq.heappush(buf, b)
            min1st = heapq.heappop(buf) if len(buf) > 0 else -1
            min2nd = heapq.heappop(buf) if len(buf) > 0 else -1
            return min1st, min2nd
        return two_min(root)[1]


ans = Solution().findSecondMinimumValue(TreeNode.from_str("[2,2,5,null,null,5,7]"))
print(ans)
