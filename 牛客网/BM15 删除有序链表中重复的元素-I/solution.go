package main
// import "fmt"
import . "nc_tools"
/*
 * type ListNode struct{
 *   Val int
 *   Next *ListNode
 * }
 */

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param head ListNode类 
 * @return ListNode类
*/
func deleteDuplicates( head *ListNode ) *ListNode {
    var result = &ListNode{Next: head}
    for head != nil && head.Next != nil {
        if head.Val == head.Next.Val {
            head.Next = head.Next.Next
        } else {
            head = head.Next
        }
    }
    return result.Next
}
