package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param nums int整型一维数组 
 * @param target int整型 
 * @return int整型
*/
func search( nums []int ,  target int ) int {
    // write code here
    var left, right = 0, len(nums)
    for left < right {
        mid := (left + right) / 2
        fmt.Println(left, mid, right)
        if nums[mid] == target {
            return mid
        } else if nums[mid] > target {
            right = mid
        } else {
            if left == mid {
                left = mid + 1
            } else {
                left = mid
            }  
        }
    }

    return -1
}
