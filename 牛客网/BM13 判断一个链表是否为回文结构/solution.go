package main
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
 * @param head ListNode类 the head
 * @return bool布尔型
*/
func isPail( head *ListNode ) bool {
    // write code here
    var result = true
    newPointer := reverseCopy(head)
    for head != nil {
        if head.Val != newPointer.Val {
            result = false
            break
        }
        head = head.Next
        newPointer = newPointer.Next
    }
    
    return result
}

// 这里只能copy，如果直接翻转，因为使用的是指针，会造成外部变量引用修改
func reverseCopy(head *ListNode) *ListNode {
    var newHead = head
    var res *ListNode
    for newHead != nil {
        res = &ListNode{Val: newHead.Val, Next: res}
        newHead = newHead.Next
    }

    return res
}
