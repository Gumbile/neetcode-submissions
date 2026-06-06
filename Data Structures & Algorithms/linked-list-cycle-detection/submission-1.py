# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checker = set()
        # if head == None:
        #     return True

        while head != None:
            # if head.val == 4:
            #     print(head.next.val)
            if head in checker:
                return True

            checker.add(head)
            head = head.next


        return False