from utils import TreeNode

from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def is_node_sym(node_a, node_b) -> bool:
            if node_a.val == node_b.val:
                if (node_a.left and node_b.right) or (not node_a.left and not node_a.right):
                    if (node_a.right and node_b.left) or (not node_a.right and not node_a.left):
                        return True
            return False

        if not root:
            return True
        if (not root.left) and (not root.right):
            return True
        if not (root.left and root.right):
            return False

        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                tmp.append(queue.popleft())
            i = 0
            j = len(tmp) - 1
            flag = True
            while i < j:
                flag = flag and is_node_sym(tmp[i], tmp[j])
                i += 1
                j -= 1
            if not flag:
                return False
            for node in tmp:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return True


tree = TreeNode.from_str("[1,2,2,null,3,3]")
print(TreeNode.to_str(tree))
ans = Solution().isSymmetric(tree)
print(ans)