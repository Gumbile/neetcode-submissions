/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
	// if list is empty
    if head == nil {
		return nil
	}

	// if list only one node
	if head.Next == nil {
		return head
	}

	var last *ListNode = nil
	curr := head
	next := head.Next

	for curr != nil {
		curr.Next = last
		last = curr 
		curr = next
		if next != nil {
		next = next.Next
		}
	}

	head = last

	return head
	

}
