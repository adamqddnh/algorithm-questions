package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 给定数组的最长严格上升子序列的长度。
 * @param arr int整型一维数组 给定的数组
 * @return int整型
 */
func LIS( arr []int ) int {
    var (
        length = len(arr)
        dp = make([]int, length)
        res = 1
    )
    if length == 0 {
        return 0
    }
    for i := 0; i < length; i++ {
        dp[i] = 1
        for j := i-1; j >= 0; j-- {
            if arr[j] < arr[i] {
                dp[i] = maxInt(dp[i], dp[j]+1)
            }
        }
        res = maxInt(res, dp[i])
    }
    return res
}

func maxInt(a, b int) int {
    if a > b {
        return a
    }

    return b
}
