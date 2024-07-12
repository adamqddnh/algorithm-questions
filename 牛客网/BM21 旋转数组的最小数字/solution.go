package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param nums int整型一维数组 
 * @return int整型
*/
func minNumberInRotateArray( nums []int ) int {
    // write code here
    var left, right = 0, len(nums) - 1
    for left < right {
        mid := (left + right) >> 1
        fmt.Println(left, mid, right)
        if nums[left] > nums[mid] {
            right = mid
        } else if nums[mid] > nums[right] {
            left = mid + 1
        } else {
            right--
        }
    }

    return nums[left]
}
