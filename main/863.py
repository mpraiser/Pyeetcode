from utils.treenode import TreeNode

from typing import List, Tuple, Optional


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ret = []

        def f(node: TreeNode, last: Optional[TreeNode] = None):
            """Convert a tree to a graph"""
            node.child = set()
            if last:
                node.child.add(last)
            if node.left:
                node.child.add(node.left)
                f(node.left, node)
            if node.right:
                node.child.add(node.right)
                f(node.right, node)

        visited = set()

        def g(node: TreeNode, depth: int = 0):
            """DFS of graph"""
            nonlocal ret, k, target
            nonlocal visited
            visited.add(node)
            if depth == k:
                ret.append(node.val)
            else:
                for c in node.child:
                    if c not in visited:
                        g(c, depth + 1)

        f(root)
        g(target)
        return ret


def preprocess(tree: str, target: int, k: int) -> Tuple[TreeNode, TreeNode, int]:
    ro = TreeNode.from_str(tree)

    def dfs(node) -> Optional[TreeNode]:
        if node.val == target:
            return node
        if node.left:
            t = dfs(node.left)
            if t:
                return t
        if node.right:
            t = dfs(node.right)
            if t:
                return t

    ta = dfs(ro)
    return ro, ta, k


ans = Solution().distanceK(*preprocess("[3,5,1,6,2,0,8,null,null,7,4]", 5, 2))
print(ans)
