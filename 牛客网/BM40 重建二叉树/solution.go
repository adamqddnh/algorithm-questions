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
 * @param preOrder int整型一维数组 
 * @param vinOrder int整型一维数组 
 * @return TreeNode类
*/
func reConstructBinaryTree( preOrder []int ,  vinOrder []int ) *TreeNode {
    // write code here
    if len(preOrder) == 0 {
        return nil
    }

    var idx = 0
    for ; idx < len(preOrder); idx++ {
        if preOrder[0] == vinOrder[idx] {
            break
        }
    }

    return &TreeNode{
        Val: preOrder[0],
        Left: reConstructBinaryTree(preOrder[1:idx+1], vinOrder[:idx]),
        Right: reConstructBinaryTree(preOrder[idx+1:], vinOrder[idx+1:]),
    }
}
