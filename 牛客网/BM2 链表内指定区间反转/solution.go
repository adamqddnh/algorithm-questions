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
 * @param m int整型
 * @param n int整型
 * @return ListNode类
 */
func reverseBetween( head *ListNode ,  m int ,  n int ) *ListNode {
    // write code here
    if !validator(head, m, n) {
        return head
    }

    var (
        result = &ListNode{Next: head}
        left = result
    )

    for i := 1; i < m; i++ {
        left = left.Next
    }
    left.Next = reverse(left.Next, n-m)

    return result.Next
}

func validator( head *ListNode ,  m int ,  n int ) bool {
    if head == nil {
        return false
    }
    if m > n || m <= 0 || n <= 0 || m > 1000 || n > 1000 {
        return false
    }

    return true
}

func reverse(head *ListNode, length int) *ListNode {
    var (
        first = head
        right = head
        left *ListNode
    )
    for i := 0; i <= length; i++ {
        fmt.Println(head.Val)
        right = head.Next
        head.Next = left
        left = head
        head = right
    }
    first.Next = right
    return left
}
