
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


if __name__ == "__main__":
    root = gen_tree([1,2,3,null,4,null,5])
    root.show()

