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
 * @param head ListNode类 
 * @return ListNode类
*/
func oddEvenList( head *ListNode ) *ListNode {
    // write code here
    var (
        curr = head
        oddCurr, evenCurr = new(ListNode), new(ListNode)
        oddHead = oddCurr
        evenHead = evenCurr
        i = 0
    )
    for curr != nil {
        i += 1
        fmt.Println(i)
        if i & 1 == 1 {
            // 奇数
            oddCurr.Next = curr
            oddCurr = oddCurr.Next
        } else {
            // 偶数
            evenCurr.Next = curr
            evenCurr = evenCurr.Next
        }
        curr = curr.Next
    }
    oddCurr.Next = nil
    evenCurr.Next = nil
    if oddCurr != nil && evenHead.Next != nil {
        oddCurr.Next = evenHead.Next
    }
    
    return oddHead.Next
}
