
class ListNode:
    def __init__(self, key =0,val=0, next=None,prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int,):
        self.cap = capacity
        self.length = 0

        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        
        self.cahce = {}
        

    def get(self, key: int) -> int:
       if key not in self.cahce:
           return -1
       else:
           node = self.cahce[key]
           self.remove(node=node)
           self.insert(node=node)
           return node.val


    def put(self, key: int, value: int) -> None:
        
        if key in self.cahce:
            node:ListNode = self.cahce[key]
            self.remove(node)
            node.val = value

            self.insert(node)
            self.cahce[key] = node
        
        else:
            
            if self.length < self.cap:
                self.length+=1
            else:
                tmp = self.left.next
                self.remove(tmp)
                del self.cahce[tmp.key]

            node = ListNode(key,value)
            self.insert(node)

            self.cahce[key] = node
            
            

    def remove(self,node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insert(self,node):
        tmp = self.right.prev
        
        tmp.next = node
        node.prev = tmp

        node.next = self.right
        self.right.prev = node
