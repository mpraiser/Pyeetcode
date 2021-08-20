from utils import TreeNode


from typing import Optional


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        def rev(node: Optional[TreeNode]):
            if not node:
                return None
            node.left, node.right = rev(node.right), rev(node.left)
            return node

        return rev(root)
