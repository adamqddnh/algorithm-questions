package main
import . "nc_tools"
/*
 * type ListNode struct{
 *   Val int
 *   Next *ListNode
 * }
 */

/**
 * 
 * @param head ListNode类 
 * @return bool布尔型
*/
func hasCycle( head *ListNode ) bool {
    // write code here
    var fast, slow = head, head
    for fast != nil && fast.Next != nil && fast.Next.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
        if slow.Val == fast.Val {
            return true
        }
    }

    return false
}
