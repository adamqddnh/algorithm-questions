/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func reverseOddLevels(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	currentLevel := []*TreeNode{root}
	levelNum := 0
	for len(currentLevel) > 0 {
		if levelNum%2 == 1 { // Odd line
			left, right := 0, len(currentLevel)-1
			for left < right {
				currentLevel[left].Val, currentLevel[right].Val = currentLevel[right].Val, currentLevel[left].Val
				left++
				right--
			}
		}

		nextLevel := make([]*TreeNode, 0)
		for _, node := range currentLevel {
            if node == nil {
                continue
            }
            if node.Left != nil {
			    nextLevel = append(nextLevel, node.Left)
            }
            if node.Right != nil {
			    nextLevel = append(nextLevel, node.Right)
            }
		}
		currentLevel = nextLevel
		levelNum++
	}

	return root
}
