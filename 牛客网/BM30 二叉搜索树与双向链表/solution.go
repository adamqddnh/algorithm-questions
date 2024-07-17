package main
import . "nc_tools"
/*
 * type TreeNode struct {
 *   Val int
 *   Left *TreeNode
 *   Right *TreeNode
 * }
 */

/**
 * 
 * @param pRootOfTree TreeNode类 
 * @return TreeNode类
*/
var pre *TreeNode

func Convert( pRootOfTree *TreeNode ) *TreeNode {
    // write code here
    if pRootOfTree == nil {
        return nil
    }
    if pRootOfTree.Left == nil && pRootOfTree.Right == nil {
        return pRootOfTree
    }
    dfs(pRootOfTree)
    for pRootOfTree.Left != nil {
        pRootOfTree = pRootOfTree.Left
    }

    return pRootOfTree
}

// 深度优先中序遍历
func dfs(root *TreeNode) {
    if root == nil {
        return
    }
    dfs(root.Left)
    root.Left = pre
    if pre != nil {
        pre.Right = root
    }
    pre = root
    dfs(root.Right)
}
