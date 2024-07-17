package main

import (
	"fmt"
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
 * @param root TreeNode类
 * @return bool布尔型
 */
func isValidBST( root *TreeNode ) bool {
    // write code here
    return dfs(root, math.MinInt, math.MaxInt)
}

func dfs(root *TreeNode, min int, max int) bool {
    fmt.Println(root, min, max)
    if root == nil {
        return true
    }
    if root.Val > max || root.Val < min {
        return false
    }
    return dfs(root.Left, min, root.Val) && dfs(root.Right, root.Val, max)
}

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func maxInt(a, b int) int {
    if a > b {
        return a
    }
    return b
}
