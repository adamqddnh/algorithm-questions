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
 * @return bool布尔型
*/
func isCompleteTree( root *TreeNode ) bool {
    // write code here
    // 判断完全二叉树思路
    // 1. 树不能存在左空右不空的分支
    // 2. 广度优先遍历时，最后一行如果出现了空节点，后续节点不能有值
    var bfsArr []*TreeNode
    var head = root
    for head != nil {
        if head.Left == nil && head.Right != nil {
            return false
        }
        bfsArr = append(bfsArr, head.Left)
        bfsArr = append(bfsArr, head.Right)

        if len(bfsArr) > 0 {
            head = bfsArr[0]
            bfsArr = bfsArr[1:]
        }
    }

    if head == nil && len(bfsArr) > 0 {
        for _, value := range bfsArr {
            if value != nil {
                return false
            }
        }
    }

    return true
}
