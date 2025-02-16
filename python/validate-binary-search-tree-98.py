# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inOrderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        current = root
        list = []
        stack = []
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


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = self.inOrderTraversal(root)

        if len(output) == 1: return True

        for i in range(1, len(output)):
            if output[i] <= output[i-1]:
                return False

        return True

