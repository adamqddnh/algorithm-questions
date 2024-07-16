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
 * @param t1 TreeNode类 
 * @param t2 TreeNode类 
 * @return TreeNode类
*/
func mergeTrees( t1 *TreeNode ,  t2 *TreeNode ) *TreeNode {
    // write code here
    if t1 == nil {
        return t2
    }
    if t2 == nil {
        return t1
    }

    t1.Val += t2.Val
    t1.Left = mergeTrees(t1.Left, t2.Left)
    t1.Right = mergeTrees(t1.Right, t2.Right)

    return t1
}
