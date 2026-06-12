# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.d = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left),height(root.right))

        self.d = max(self.d,height(root.left) + height(root.right))

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return self.d
