func minOperations(boxes string) []int {
    var (
		length = len(boxes)
		leftBallNum, leftNeedMoveNum   int
		rightBallNum, rightNeedMoveNum int
		res = make([]int, length)
	)
	for left := 0; left < length; left++ {
		res[left] += leftNeedMoveNum
		if boxes[left] == '1' {
			leftBallNum += 1
		}
		leftNeedMoveNum += leftBallNum

		right := length - left - 1
		res[right] += rightNeedMoveNum
		if boxes[right] == '1' {
			rightBallNum += 1
		}
		rightNeedMoveNum += rightBallNum
	}
	
    return res
}
