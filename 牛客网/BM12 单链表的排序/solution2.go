package main

import (
	"fmt"
	. "nc_tools"
	"sort"
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
 * @param head ListNode类 the head node
 * @return ListNode类
 */
func sortInList( head *ListNode ) *ListNode {
    // write code here
    var (
        arr = []int{}
        newHead = &ListNode{}
        result = newHead
    )
    for head != nil {
        arr = append(arr, head.Val)
        head = head.Next
    }
    sort.Slice(arr, func(i, j int) bool {
        if arr[i] >= arr[j] {
            return false
        }
        return true
    })

    for i := 0; i < len(arr); i++ {
        curr := &ListNode{Val: arr[i]}
        newHead.Next = curr
        newHead = newHead.Next
    }
    fmt.Println(arr)

    return result.Next
}
