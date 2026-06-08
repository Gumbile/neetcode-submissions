# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None


        curr = head
        size = 0 
        
        while curr:
            size+=1
            curr = curr.next


        indexFromStart = size - n + 1


        # removing head
        if indexFromStart == 1:
            tmp = head.next
            head.next = None
            head = tmp

        
        # any other postion
        else:
            
            prev = head
            curr = head.next
            
            for i in range(2,size + 1):
            
                if indexFromStart == i:
                    prev.next = curr.next
                    curr.next = None
                    break

                prev = curr
                curr = curr.next




        return head