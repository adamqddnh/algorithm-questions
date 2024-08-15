package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * longest common subsequence
 * @param s1 string字符串 the string
 * @param s2 string字符串 the string
 * @return string字符串
*/
func LCS( s1 string ,  s2 string ) string {
    var (
        l1, l2 = len(s1), len(s2)
        dp = make([][]string, l1+1)
    )
    for k := range dp {
        dp[k] = make([]string, l2+1)
    }

    for i := 1; i <= l1; i++ {
        for j := 1; j<= l2; j++ {
            if s1[i-1] == s2[j-1] {
                // 如果两个字符相同，增加到dp数组中
                dp[i][j] = fmt.Sprintf("%s%s", string(dp[i-1][j-1]), string(s1[i-1]))
            } else {
                // 如果两个字符不相同，找到之前较长的子字符串
                if len(dp[i-1][j]) > len(dp[i][j-1]) {
                    dp[i][j] = dp[i-1][j]
                } else {
                    dp[i][j] = dp[i][j-1]
                }
            }
        }
    }
    res := dp[l1][l2]
    if res == "" {
        res = "-1"
    }
    return res
}
