func waysToSplitArray(nums []int) int {
    var (
        left, right = 0, 0
        res = 0
    )
    for _, num := range nums {
        right += num
    }
    for i := 0; i < len(nums) - 1; i++ {
        left += nums[i]
        right -= nums[i]
        if left >= right {
            res += 1
        }
    } 

    return res
}
