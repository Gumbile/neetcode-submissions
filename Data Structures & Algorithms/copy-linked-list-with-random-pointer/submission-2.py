"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None


        fakeHead = Node(head.val)
        
        
        curr = head.next
        fakeCurr = fakeHead

        hm = {head:fakeHead}

        while curr:
            fakeCurr.next = Node(curr.val)
            hm[curr] = fakeCurr.next
            curr = curr.next
            fakeCurr = fakeCurr.next


        curr = head
        fakeCurr = fakeHead
        
        while curr:
            
            if curr.random == None:
                fakeCurr.random = None
        
            else:
                tmp = hm[curr.random]
                fakeCurr.random = tmp
            
            curr = curr.next
            fakeCurr = fakeCurr.next

        return fakeHead