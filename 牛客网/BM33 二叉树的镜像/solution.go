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
 * @param pRoot TreeNode类 
 * @return TreeNode类
*/
func Mirror( pRoot *TreeNode ) *TreeNode {
    // write code here
    if pRoot == nil {
        return pRoot
    }

    temp := pRoot.Left
    pRoot.Left = pRoot.Right
    pRoot.Right = temp

    Mirror(pRoot.Left)
    Mirror(pRoot.Right)

    return pRoot
}
