package main
import "fmt"
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
 * @param head1 ListNode类 
 * @param head2 ListNode类 
 * @return ListNode类
*/
func addInList( head1 *ListNode ,  head2 *ListNode ) *ListNode {
    // write code here
    var (
        newHead1 = reverse(head1)
        newHead2 = reverse(head2)
        carry = 0
        res *ListNode
    )
    fmt.Println(newHead1)
    fmt.Println(newHead2)
    for newHead1 != nil || newHead2 != nil {
        num := carry
        if newHead1 != nil {
            num += newHead1.Val
            newHead1 = newHead1.Next
        }
        if newHead2 != nil {
            num += newHead2.Val
            newHead2 = newHead2.Next
        }
        if num >= 10 {
            carry = 1
            num -= 10
        } else {
            carry = 0
        }
        res = &ListNode{Val: num, Next: res}
    }
    if carry > 0 {
        res = &ListNode{Val: carry, Next: res}
    }
    return res
}

func reverse(head *ListNode) *ListNode {
    var res *ListNode
    var curr = head
    for curr != nil {
        curr = head.Next
        head.Next = res
        res = head
        head = curr
    }
    return res
}
