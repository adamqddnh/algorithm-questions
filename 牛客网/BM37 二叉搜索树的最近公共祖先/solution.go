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
 * @param p int整型 
 * @param q int整型 
 * @return int整型
*/
func lowestCommonAncestor( root *TreeNode ,  p int ,  q int ) int {
    // write code here
    for root != nil {
        if p < root.Val && q < root.Val {
            root = root.Left
        } else if root.Val < p && root.Val < q {
            root = root.Right
        } else {
            return root.Val
        }
    }

    return root.Val
}
