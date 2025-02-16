
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def pruning(root):
            if root is None: return None

            pruning(root.left)
            pruning(root.right)
            if root.val == 0 and root.left is None and root.right is None:
                return None

        pruning(root)
        return root