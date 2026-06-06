# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return


        fast:ListNode = head 
        slow:ListNode = head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None


        prev = None
        curr = secondHalf

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        
        first = head


        while prev:
            tmpFront,tmpRear = first.next, prev.next

            first.next = prev
            prev.next = tmpFront


            first = tmpFront
            prev = tmpRear

            