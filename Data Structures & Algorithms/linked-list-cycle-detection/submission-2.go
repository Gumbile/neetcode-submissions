/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
    checker := make(map[*ListNode]struct{})

    for head != nil{
        if _,ok :=checker[head]; ok{
            return true
        }

        checker[head] = struct{}{}

        head = head.Next

    }


    return false
}
