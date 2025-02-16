"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        list = []

        def preOrderTraverse(root):
            if root is None: return
            list.append(root.val)

            for child in root.children:
                preOrderTraverse(child)

        preOrderTraverse(root)
        return list