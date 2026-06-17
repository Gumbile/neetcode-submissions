# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {}

        for i in range(len(inorder)):
            indexes[inorder[i]] = i
        

        def dfs(idx,l,r):
            if l > r:
                return None
            
            node = TreeNode(preorder[idx])
            
            idxInOrder = indexes[preorder[idx]]
           
            left_size = idxInOrder - l
            
            left = dfs(idx+1,   l,  idxInOrder - 1)
            right = dfs(left_size + idx + 1,   idxInOrder+1    ,r)

            node.left = left
            node.right = right

            return node


        root = dfs(0,0,len(preorder) - 1)

        return root

