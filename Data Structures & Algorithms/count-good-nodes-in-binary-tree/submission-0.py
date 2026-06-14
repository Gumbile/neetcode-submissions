# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(root,maxN):
            if not root:
                return

            if root.val >= maxN:
                res.append(root.val)
                maxN = root.val

            dfs(root.left,maxN)
            dfs(root.right,maxN)

        dfs(root,root.val)

        return len(res)