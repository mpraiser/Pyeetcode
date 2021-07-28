from utils.treenode import TreeNode

from typing import List, Tuple, Optional


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ret = []
        visited = set()

        def bind_parent(node: TreeNode, parent: Optional[TreeNode] = None):
            """Convert a tree to a graph"""
            node.parent = None
            if parent:
                node.parent = parent
            if node.left:
                bind_parent(node.left, node)
            if node.right:
                bind_parent(node.right, node)

        def dfs(node: TreeNode, depth: int = 0):
            """DFS of graph"""
            nonlocal ret, visited, k, target
            visited.add(node)
            if depth == k:
                ret.append(node.val)
            else:
                for c in (node.parent, node.left, node.right):
                    if c and (c not in visited):
                        dfs(c, depth + 1)

        bind_parent(root)
        dfs(target)
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
