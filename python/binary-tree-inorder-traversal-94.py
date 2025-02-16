# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        stack = []
        current = root
        while current is not None:
            stack.append(current)
            current = current.left

        while stack:
            current = stack.pop()
            list.append(current.val)
            current = current.right

            while current is not None:
                stack.append(current)
                current = current.left
        return list
