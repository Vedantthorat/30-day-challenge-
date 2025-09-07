class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    # Base Case
    if not root or root == p or root == q:
        return root

    # Search left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both sides return non-null, current root is LCA
    if left and right:
        return root

    # Otherwise return the non-null side
    return left if left else right
