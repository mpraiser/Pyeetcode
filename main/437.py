# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from utils.treenode import TreeNode

from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        sums = defaultdict(int)  # prefix sum
        sums[0] = 1
        result = 0

        def dfs(node: TreeNode, s: int):
            """returns list of all possible path sums"""
            nonlocal result, sums
            s += node.val
            result += sums[s - targetSum]
            sums[s] += 1
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)
            sums[s] -= 1

        dfs(root, 0)
        return result


cases = [
    ("[10,5,-3,3,2,null,11,3,-2,null,1]", 8),
    ("[5,4,8,11,null,13,4,7,2,null,null,5,1]", 22)
]
for case in cases:
    root = TreeNode.from_str(case[0])
    ans = Solution().pathSum(root, case[1])
    print(ans)
