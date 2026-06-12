# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root or not subRoot:
            return False
        
        res = False

        def checkSame(p,q):
            if not p and not q :
                return True
            elif p and q and p.val == q.val:
                return checkSame(p.left,q.left) and checkSame(p.right,q.right)
            else:
                return False

        if (root.val == subRoot.val) and not res:
            res = checkSame(root,subRoot)

        return res or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

       