# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMax(self,val,l,r):
        if max(l,r) < 0:
            return val
        if min(l,r) > 0:
            return val + l + r

        return val + max(l,r)

    def returnMax(self,val,l,r):
        if max(l,r) < 0:
            return val
        

        return val + max(l,r)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-1001]

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            max_sum[0] = max(max_sum[0],self.getMax(node.val,left,right))

            return self.returnMax(node.val,left,right)


        last_val = dfs(root)
        
        return max(max_sum[0],last_val)

