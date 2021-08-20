from utils import TreeNode

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """BFS"""
        if not root:
            return []
        queue = deque()
        queue.append((root, 0))
        ret = [[]]
        while queue:
            node, depth = queue.popleft()
            while depth >= len(ret):
                ret.append([])
            ret[depth].append(node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return ret
