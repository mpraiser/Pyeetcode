from utils import TreeNode

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> list[int]:
        """BFS"""
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ret = []
        while queue:
            node = queue.popleft()
            ret.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ret
