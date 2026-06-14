# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       
        
        res = []

        def bfs(root,level):



            if not root:
                return None

            if len(res) <= level:
                res.append([])

            res[level].append(root.val)

            bfs(root.left,level+1)
            bfs(root.right,level+1)


        bfs(root,0)

        return res


 

            