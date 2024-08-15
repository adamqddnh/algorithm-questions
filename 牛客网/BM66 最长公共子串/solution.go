package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * longest common substring
 * @param str1 string字符串 the string
 * @param str2 string字符串 the string
 * @return string字符串
*/
func LCS( str1 string ,  str2 string ) string {
    var (
        l1, l2 = len(str1), len(str2)
        dp = make([][]string, l1+1)
        maxLength = 0
        res = ""
    )
    for k := range dp {
        dp[k] = make([]string, l2+1)
    }
    for i := 1; i <= l1; i++ {
        for j := 1; j <= l2; j++ {
            if str1[i-1] == str2[j-1] {
                dp[i][j] = fmt.Sprintf("%s%s", dp[i-1][j-1], string(str1[i-1]))
                if len(dp[i][j]) > maxLength {
                    maxLength = len(dp[i][j])
                    res = dp[i][j]
                }
            } else {
                dp[i][j] = ""
            }
        }
    }

    return res
}
