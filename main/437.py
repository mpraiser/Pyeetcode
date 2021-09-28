# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from utils.treenode import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        path = [0]
        result = 0

        def dfs(node: TreeNode):
            """returns list of all possible path sums"""
            nonlocal result
            for i in range(len(path)):
                if path[-1] - path[i] == targetSum - node.val:
                    result += 1
            if node.left:
                path.append(path[-1] + node.val)
                dfs(node.left)
                path.pop()
            if node.right:
                path.append(path[-1] + node.val)
                dfs(node.right)
                path.pop()

        dfs(root)
        return result


cases = [
    ("[10,5,-3,3,2,null,11,3,-2,null,1]", 8),
    ("[5,4,8,11,null,13,4,7,2,null,null,5,1]", 22)
]
for case in cases:
    root = TreeNode.from_str(case[0])
    ans = Solution().pathSum(root, case[1])
    print(ans)
