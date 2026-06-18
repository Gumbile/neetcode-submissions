# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root: Optional[TreeNode]) -> str:
            if not root:
                return "$#"
            
            mystr = "$"+str(root.val)

            return mystr + dfs(root.left)+"|"+dfs(root.right)

        s = dfs(root)
        print(s)
        return s
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        

        end = self.getIndex(data) 
        root_val = self.getEle(data,end)
        if root_val == -1001:
            return None
        root = TreeNode(root_val)

        stack = []
        stack.append(root)

        data = data[end:]
        # node  = root

        
        while data:
            
            node = stack[-1]
            rightflg = False
            
            if data[0] == "|":
                data = data[1:]
                rightflg = True


            end = self.getIndex(data) 
            node_val = self.getEle(data,end)
            
            data = data[end:]
            if node_val == -1001:
                if rightflg:
                    stack.pop()
                continue
            
            
            newNode = TreeNode(node_val)

            if not rightflg:
                node.left = newNode
            else:
                node.right = newNode
                stack.pop()
                
            stack.append(newNode)

        return root


    def getIndex(self,s:str)->int:
        i = 1
        size = len(s)
        
        while i < size:
            if s[i] == "$" or s[i] == "|":
                break
            i+=1

        return i

    def getEle(self,s:str,end:int) -> int:
        if s[1] == '#':
            return -1001

        return int(s[1:end])
