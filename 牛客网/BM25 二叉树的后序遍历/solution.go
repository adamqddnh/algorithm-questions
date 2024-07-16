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
 * @return int整型一维数组
*/
func postorderTraversal( root *TreeNode ) []int {
    // write code here
    var res []int
    postorder(&res, root)
    return res
}

func postorder(res *[]int, root *TreeNode) {
    if root == nil {
        return
    }
    postorder(res, root.Left)
    postorder(res, root.Right)
    *res = append(*res, root.Val)
}
