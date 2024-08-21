package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param matrix int整型二维数组 the matrix
 * @return int整型
*/
func minPathSum( matrix [][]int ) int {
    var (
        l1 = len(matrix)
        l2 = len(matrix[0])
        dp = make([][]int, l1+1)
    )
    for i := 0; i <= l1; i++ {
        dp[i] = make([]int, l2+1)
    }
    for i := 1; i < l1+1; i++ {
        for j := 1; j < l2+1; j++ {
            if i == 1 {
                dp[i][j] = dp[i][j-1] + matrix[i-1][j-1]
            } else if j == 1 {
                dp[i][j] = dp[i-1][j] + matrix[i-1][j-1]
            } else {
                dp[i][j] = minInt(dp[i-1][j], dp[i][j-1]) + matrix[i-1][j-1]
            }
        }
    }
    fmt.Println(dp)

    return dp[l1][l2]
}

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}
