
null = None

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def gen_tree(vals: list):
    if not vals:
        return None
    
    def f(node, p):
        p_l = 2*p + 1
        p_r = 2*p + 2
        if 0 <= p_l < len(vals) and vals[p_l]:
            node.left = TreeNode(vals[p_l], None, None)
            f(node.left, p_l)
        if 0 <= p_r < len(vals) and vals[p_r]:
            node.right = TreeNode(vals[p_r], None, None)
            f(node.right, p_r)

    root = TreeNode(vals[0], None, None)
    f(root, 0)
    return root


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.depth_x = None
        self.depth_y = None
        self.x = x
        self.y = y
        self.same_parent = False
        self.helper(root, 0)
        return (not self.same_parent) and self.depth_x == self.depth_y

    def helper(self, node, depth):
        """
        Return:
            exception (same parent) happens
        """
        if node.left and node.right:
            if (node.left.val == self.x and node.right.val == self.y) or \
                (node.left.val == self.y and node.right.val == self.x):
                self.same_parent = True
        if node.val == self.x:
            self.depth_x = depth
        elif node.val == self.y:
            self.depth_y = depth
        if (not self.depth_x) or (not self.depth_y):
            if node.left:
                self.helper(node.left, depth+1)
            if node.right:
                self.helper(node.right, depth+1)
    

        

x = Solution()
# ans = x.isCousins(gen_tree([1,2,3,null,4,null,5]), 5, 4)
# ans = x.isCousins(gen_tree([1,2,3,4]), 3, 4)
ans = x.isCousins(gen_tree([1,2,3,null,null,4,5]), 5, 4)
print(ans)