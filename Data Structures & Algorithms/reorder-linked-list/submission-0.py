# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        front = head 
        rear = head
        tmp = head

        length = 0
        while tmp:
            length +=1
            tmp = tmp.next

        if length <= 2:
            return

        half = (length + 1) // 2

        prev = None
        # tmp = head
        # reversing list after half
        for i in range(1,length+1):
            
            if i > half:
                tmp = rear.next
                rear.next = prev
                prev = rear
                if tmp:
                    rear = tmp
            else:
                prev = rear
                rear = rear.next
        
        
        # printListNode(head)
        
        nextFront = None
        nextRear = None 

        while True:

            if front.next == rear:
                rear.next = None
                break

            nextFront = front.next
            nextRear = rear.next

            front.next = rear
            rear.next = nextFront

            front = nextFront
            rear = nextRear

            if front == rear:
                front.next = None
                break

            