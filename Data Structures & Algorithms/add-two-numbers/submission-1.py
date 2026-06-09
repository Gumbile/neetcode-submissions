# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        l3 = head
        carry = 0

        lastNode = None

        while l1 and l2:
            add = carry + l2.val + l1.val

            if add > 9:
                carry = add // 10
            else:
                carry = 0
            l3.val = add % 10

            l1,l2 = l1.next , l2.next
            
            lastNode = l3
            
            l3.next = ListNode()
            l3 = l3.next


        while l1:
            add = carry + l1.val

            if add > 9:
                carry = add // 10
            else:
                carry = 0
            l3.val = add % 10

            l1= l1.next 
            
            lastNode = l3
            
            l3.next = ListNode()
            l3 = l3.next
        
        while l2:
            add = carry + l2.val

            if add > 9:
                carry = add // 10
            else:
                carry = 0
            l3.val = add % 10

            l2= l2.next 
            
            lastNode = l3
            
            l3.next = ListNode()
            l3 = l3.next

        
        if carry != 0:
            l3.val = carry
        else:
            lastNode.next = None


        return head