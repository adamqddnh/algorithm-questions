package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param nums int整型一维数组 
 * @return int整型
*/
func minNumberDisappeared( nums []int ) int {
    // 思路，因为空间复杂度O(1)，时间复杂度O(n)，因此排序和使用map记录的方式不适用
    // 换一种思路，如果元素没有缺失，那么nums数组中的元素在排序后一定等于其数组下标
    var (
        res = 0
        length = len(nums)
    )
    for k := range nums {
        for nums[k] > 0 && nums[k] <= length && nums[k] != nums[nums[k]-1] {
            nums[k], nums[nums[k]-1] = nums[nums[k]-1], nums[k]
        }
    }

    for k, num := range nums {
        if k != num - 1 {
            res = k + 1
            break
        } 
    }
    if res == 0 {
        res = length + 1
    }

    return res
}
