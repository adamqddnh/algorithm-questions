package main

import (
	// "fmt"
)

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 求二叉树的右视图
 * @param preOrder int整型一维数组 先序遍历
 * @param inOrder int整型一维数组 中序遍历
 * @return int整型一维数组
 */
func solve( preOrder []int ,  inOrder []int ) []int {
    // write code here
    root := buildTree(preOrder, inOrder)
    res := bfs(root)
    return res
}

type TreeNode1 struct{
    Val   int
    Left  *TreeNode1
    Right *TreeNode1
}

var nums = []int{}

func buildTree(preOrder []int ,  inOrder []int) *TreeNode1 {
    if len(preOrder) == 0 {
        return nil
    }
    idx := 0
    for ; idx < len(inOrder); idx++ {
        if preOrder[0] == inOrder[idx] {
            break
        }
    }

    return &TreeNode1{
        Val: preOrder[0],
        Left: buildTree(preOrder[1:idx+1], inOrder[0:idx]),
        Right: buildTree(preOrder[idx+1:], inOrder[idx+1:]),
    }
}

func bfs(root *TreeNode1) []int {
    var (
        res []int
        queue []*TreeNode1
    )
    if root == nil {
        return res
    }
    res = append(res, root.Val)
    if root.Left != nil {
        queue = append(queue, root.Left)
    }
    if root.Right != nil {
        queue = append(queue, root.Right)
    }
    for len(queue) > 0 {
        tmpQueue := []*TreeNode1{}
        for i := 0; i < len(queue); i++ {
            if queue[i].Left != nil {
                tmpQueue = append(tmpQueue, queue[i].Left)
            }
            if queue[i].Right != nil {
                tmpQueue = append(tmpQueue, queue[i].Right)
            }
        }
        res = append(res, queue[len(queue)-1].Val)
        queue = tmpQueue
    }
    return res
}
