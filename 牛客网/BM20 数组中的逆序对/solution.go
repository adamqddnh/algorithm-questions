package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param nums int整型一维数组 
 * @return int整型
*/
func InversePairs( nums []int ) int {
    return merge(nums, 0, len(nums)-1) % 1000000007
}

func merge(nums []int, start, end int) int {
    var res = 0
    if start >= end {
        return res
    }
    mid := (start + end) / 2
    res = merge(nums, start, mid) + merge(nums, mid+1, end)

    tempArr := []int{}
    left, right := start, mid+1
    for left <= mid && right <= end {
        // if nums[left] > nums[right] {
        //     res += right - mid
        //     tempArr = append(tempArr, nums[right])
        //     right++
        // } else {
        //     tempArr = append(tempArr, nums[left])
        //     left++
        // }
        if nums[left] <= nums[right] {              // 当左元素小于等于右元素 说明在右半部分的右元素的左边的元素均小于左元素
            tempArr = append(tempArr, nums[left])
            res += right - (mid + 1)                // 因此cnt需要加上右元素左边部分的元素数量
            left++
        } else {
            tempArr = append(tempArr, nums[right])  // 当左元素大于右元素 不能直接开始计数 
            right++                                 // 因为不确定右元素右边还有没有比左元素更小的元素
        }
    }

    for ; left <= mid; left++ {                     // 处理另一半未遍历完的数据
        tempArr = append(tempArr, nums[left])
        res += end - mid
    }
    for ; right <= end; right++ {   // 同上
        tempArr = append(tempArr, nums[right])
    }
    for i := start; i <= end; i++ { // 将排序好的数组元素依次赋值给nums数组
        nums[i] = tempArr[i - start]
    }

    fmt.Println(tempArr, res)

    return res
}
