from typing import List
from collections import deque

import utils.leetcodec as lc


class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def to_str(root) -> str:
        return lc.serialize(TreeNode.to_list(root))

    @staticmethod
    def to_list(root) -> List:
        if not root:
            return []

        values = [root.val]
        dq = deque()
        dq.append((1, root))
        max_depth = 1
        while len(dq) > 0:
            d, node = dq.popleft()
            if d > max_depth:
                max_depth = d
            if node.left:
                values.append(node.left.val)
                dq.append((d+1, node.left))
            else:
                values.append(None)
            if node.right:
                values.append(node.right.val)
                dq.append((d+1, node.right))
            else:
                values.append(None)

        return values[:2 ** max_depth - 1]

    @staticmethod
    def from_str(data: str):
        return TreeNode.from_list(lc.parse(data))

    @staticmethod
    def from_list(values: List):
        if not values:
            return None

        root = TreeNode(values[0])
        ptr = 1
        dq = deque()
        dq.append(root)

        while len(dq) > 0:
            node = dq.popleft()
            if ptr + 1 < len(values):
                if values[ptr] is not None:
                    node.left = TreeNode(values[ptr])
                    dq.append(node.left)
                ptr += 1
                if values[ptr] is not None:
                    node.right = TreeNode(values[ptr])
                    dq.append(node.right)
                ptr += 1

        return root


if __name__ == "__main__":
    r = TreeNode.from_str("[1,2,3,null,null,4,5]")
    print(TreeNode.to_str(r))

