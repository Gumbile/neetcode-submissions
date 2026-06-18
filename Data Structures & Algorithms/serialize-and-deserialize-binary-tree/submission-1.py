# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(root: Optional[TreeNode]) -> str:
            
            if not root:
                res.append("#")
                return

            res.append(str(root.val))
            dfs(root.left)    
            dfs(root.right)

        dfs(root)
        return ",".join(res)    
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.index = 0

        arr = data.split(",")
        size = [len(arr)]

        def dfs():
            
            if self.index == size[0]:
                return None


            val = arr[self.index]
            self.index+=1

            if val == "#":
                return None
            
            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()