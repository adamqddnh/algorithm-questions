package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 解码
 * @param nums string字符串 数字串
 * @return int整型
*/
func solve( nums string ) int {
    var dp = make([]int, len(nums)+1)
    if nums == "0" {
        return 0
    }
    dp[0] = 1
    for i := 1; i <= len(nums); i++ {
        dp[i] = dp[i-1] // 默认只翻译nums[i]，这样dp[i]与dp[i-1]翻译的方案数相同
        if i > 1 {
            tempNum := (nums[i-2] - '0') * 10 + nums[i-1] - '0'
            if nums[i-1] - '0' == 0 {
                dp[i] = 0 // 题出的贼傻逼，边界条件不说清楚，这个判断非常重要，用来去掉类似30,40这种不合法的编码
            }
            if tempNum >= 10 && tempNum <= 26 {
                dp[i] += dp[i-2]
            }
            if tempNum == 0 {
                return 0
            }
        }
    }
    fmt.Println(dp)

    return dp[len(dp)-1]
}
