from utils import TreeNode

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """BFS"""
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ret = []
        depth = 0
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if depth % 2 == 1:
                level = level[::-1]
            ret.append(level)
            depth += 1
        return ret
