package main

import (
	// "fmt"
	"math"
	. "nc_tools"
)

/*
 * type TreeNode struct {
 *   Val int
 *   Left *TreeNode
 *   Right *TreeNode
 * }
 */

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 *
 * @param pRoot TreeNode类
 * @return bool布尔型
 */
func IsBalanced_Solution( pRoot *TreeNode ) bool {
    // write code here
    if pRoot == nil {
        return true
    }
    leftHight := hight(pRoot.Left)
    rightHight := hight(pRoot.Right)

    if int(math.Abs(float64(leftHight - rightHight))) > 1 {
        return false
    }

    return IsBalanced_Solution(pRoot.Left) && IsBalanced_Solution(pRoot.Right)
}

func hight(root *TreeNode) int {
    if root == nil {
        return 0
    }
    return maxInt(hight(root.Left), hight(root.Right)) + 1
}

func maxInt(a, b int) int {
    if a > b {
        return a
    }
    return b
}
