package main
import "fmt"
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
 * @param o1 int整型 
 * @param o2 int整型 
 * @return int整型
*/
func lowestCommonAncestor( root *TreeNode ,  o1 int ,  o2 int ) int {
    // write code here
    var res int
    path1 := dfs(root, o1, []int{})
    path2 := dfs(root, o2, []int{})
    fmt.Println(path1)
    fmt.Println(path2)
    for i := 0; i <= minInt(len(path1), len(path2)) - 1; i++ {
        if path1[i] == path2[i] {
            res = path1[i]
        }
    }
    
    return res
}

func dfs(head *TreeNode, target int, path []int) []int {
    var res []int
    if head == nil {
        return res
    }
    path = append(path, head.Val)
    if head.Val == target {
        return path
    }
    res = dfs(head.Left, target, path)
    if len(res) > 0 {
        return res
    }
    res = dfs(head.Right, target, path)
    return res
}

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}
