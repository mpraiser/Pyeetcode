from utils import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        def f(a, b) -> bool:
            if (not a) or (not b):
                return False
            return (a.val == b.val and g(a, b)) or f(a.left, b) or f(a.right, b)

        def g(a, b) -> bool:
            if (not a) or (not b):
                return False
            return a.val == b.val and (not b.left or g(a.left, b.left)) and (not b.right or g(a.right, b.right))

        return f(A, B)
