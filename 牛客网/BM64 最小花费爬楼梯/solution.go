package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param cost int整型一维数组 
 * @return int整型
*/
func minCostClimbingStairs( cost []int ) int {
    var (
        length = len(cost)
        minRes = make([]int, length)
    )
    if length == 1 {
        return cost[0]
    }
    minRes[0] = cost[0]
    minRes[1] = cost[1]

    for i := 2; i < len(cost); i++ {
        minRes[i] = minInt(minRes[i-1]+cost[i], minRes[i-2]+cost[i])
    }
    fmt.Println(minRes)

    return minInt(minRes[length-1], minRes[length-2])
}

func minInt(a, b int) int {
    if a < b {
        return a
    }

    return b
}
