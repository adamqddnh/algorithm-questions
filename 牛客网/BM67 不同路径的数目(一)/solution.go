package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param m int整型 
 * @param n int整型 
 * @return int整型
*/
func uniquePaths( m int ,  n int ) int {
    var (
        dp = make([][]int, m+1)
    )
    for k := range dp {
        dp[k] = make([]int, n+1)
    }
    dp[1][1] = 1
    for i := 1; i <= m; i++ {
        for j := 1; j<= n; j++ {
            if i == 1 && j == 1 {
                continue
            }
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        }
    }
    fmt.Println(dp)

    return dp[m][n]
}
