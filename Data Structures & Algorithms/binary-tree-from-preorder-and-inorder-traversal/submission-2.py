# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {val: i for i, val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            node = TreeNode(root_val)
            self.pre_idx += 1

            mid = indexes[root_val]

            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)

            return node

        return dfs(0, len(preorder) - 1)
