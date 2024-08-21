package main

import (
	"fmt"
	"math"
)

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 最少货币数
 * @param arr int整型一维数组 the array
 * @param aim int整型 the target
 * @return int整型
 */
func minMoney( arr []int ,  aim int ) int {
    var dp = make([]int, aim+1)
    if aim == 0 {
        return 0
    }

    for i := range dp {
        dp[i] = math.MaxInt32
    }
    dp[0] = 0
    for i := 1; i <= aim; i++ {
        for _, coin := range arr {
            if coin <= i {
                dp[i] = minInt(dp[i], dp[i-coin]+1)
            }
        }
    }
    fmt.Println(dp)
    if dp[len(dp)-1] == math.MaxInt32 {
        return -1
    }

    return dp[len(dp)-1]
}

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}
