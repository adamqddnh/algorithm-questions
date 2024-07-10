package main

import (
	"fmt"
	. "nc_tools"
)

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
    // write code here
    var result = &ListNode{Next: head}
    var pre = result
    var isDuplicate = false
    for head != nil && head.Next != nil {
        fmt.Println(head.Val)
        fmt.Println(pre.Val)
        if head.Val == head.Next.Val {
            isDuplicate = true
            head = head.Next
        } else {
            if isDuplicate {
                pre.Next = head.Next
                head = head.Next
                isDuplicate = false
            } else {
                pre = pre.Next
                head = head.Next
            }
        }
    }
    if isDuplicate {
        pre.Next = head.Next
    }

    return result.Next
}
