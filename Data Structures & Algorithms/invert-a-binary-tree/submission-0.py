# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def reverseTree(root):
            if root == None:
                return None
            
            root.right = reverseTree(root.right)
            root.left = reverseTree(root.left)

            root.left,root.right = root.right,root.left

            return root

        root = reverseTree(root)

        return root
        

            