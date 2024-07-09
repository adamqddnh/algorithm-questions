package main

import (
	// "fmt"
	. "nc_tools"
)

/*
 * type ListNode struct{
 *   Val int
 *   Next *ListNode
 * }
 */

/**
 *
 * @param pHead1 ListNode类
 * @param pHead2 ListNode类
 * @return ListNode类
 */
func FindFirstCommonNode( pHead1 *ListNode ,  pHead2 *ListNode ) *ListNode {
    // write code here
    var (
        p1, p2 = pHead1, pHead2
        length1, length2 = 0, 0
    )
    for p1 != nil {
        p1 = p1.Next
        length1 += 1
    }
    for p2 != nil {
        p2 = p2.Next
        length2 += 1
    }
    if length1 > length2 {
        for i := 0; i < length1 - length2; i++ {
            pHead1 = pHead1.Next
        }
    } else {
        for i := 0; i < length2 - length1; i++ {
            pHead2 = pHead2.Next
        }
    }

    for pHead1 != nil && pHead2 != nil {
        if pHead1.Val == pHead2.Val {
            return pHead1
        }
        pHead1 = pHead1.Next
        pHead2 = pHead2.Next
    }

    return nil
}
