/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    var head *ListNode
	var tmp *ListNode
	
	for list1 != nil && list2 != nil {
		var tmp2 *ListNode
		if list1.Val < list2.Val {
			tmp2 = list1
			list1 = list1.Next
		}else{
			tmp2 = list2
			list2 = list2.Next
		}
		
		if head == nil {
			head = tmp2
			tmp = tmp2
			continue
		}

		tmp.Next = tmp2
		tmp = tmp.Next
		// fmt.Println(head.Val,tmp.Val,tmp2.Val)
	}


	for list1 != nil {
		if head == nil {
			head = list1
			tmp = list1
		
		}else{
			tmp.Next = list1
			tmp = tmp.Next
		}
		
		list1 = list1.Next
	}
	
	for list2 != nil {
		if head == nil {
			head = list2
			tmp = list2
		
		}else{
			tmp.Next = list2
			tmp = tmp.Next
		}
		list2 = list2.Next
	}

	return head
}
