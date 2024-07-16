package main
// import "fmt"
import . "nc_tools"
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
 * @return int整型
*/
func maxDepth( root *TreeNode ) int {
    // write code here
    if root == nil {
        return 0
    }

    return maxInt(maxDepth(root.Left), maxDepth(root.Right)) + 1
}

func maxInt(a, b int) int {
    if a > b {
        return a
    }
    return b
}
