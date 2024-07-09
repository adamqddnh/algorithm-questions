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
 * @param pHead1 ListNode类 
 * @param pHead2 ListNode类 
 * @return ListNode类
*/
func Merge( pHead1 *ListNode ,  pHead2 *ListNode ) *ListNode {
    // write code here
    var (
        result = &ListNode{}
        curr = result
    )
    for pHead1 != nil && pHead2 != nil {
        if pHead1.Val < pHead2.Val {
            curr.Next = pHead1
            pHead1 = pHead1.Next
        } else {
            curr.Next = pHead2
            pHead2 = pHead2.Next
        }
        curr = curr.Next
    }
    if pHead1 != nil {
        curr.Next = pHead1
    }
    if pHead2 != nil {
        curr.Next = pHead2
    }
    fmt.Println(result.Next)
    return result.Next
}
