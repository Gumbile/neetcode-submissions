# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        

        small = [min(p.val,q.val)]
        big = [max(p.val,q.val)]


        def binarySearch(root):
            if root.val >= small[0] and root.val <= big[0]:
                return root

            if root.val < small[0]:
                return binarySearch(root.right)

            if root.val > big[0]: 
                return binarySearch(root.left)

        
        return binarySearch(root)
