# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt= [0]
        val = [-1]
        def in_order(root):
            if not root:
                return 
            
            if val[0] != -1:
                return
            
            in_order(root.left)
            cnt[0] +=1
            if cnt[0] == k:
                val[0] = root.val
                return

            in_order(root.right)
            

        in_order(root)
        return val[0]
