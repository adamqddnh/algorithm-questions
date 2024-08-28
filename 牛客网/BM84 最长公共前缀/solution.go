package main
import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param strs string字符串一维数组 
 * @return string字符串
*/
func longestCommonPrefix( strs []string ) string {
    // write code here
    if len(strs) == 0 {
        return ""
    }
    var res = strs[0]
    for i := 1; i < len(strs); i++ {
        var short, long string
        if len(res) < len(strs[i]) {
            short, long = res, strs[i]
        } else {
            short, long = strs[i], res 
        }
        res = short
        for j := 0; j < len(short); j++ {
            if short[j] == long[j] {
                continue
            } else {
                res = short[:j]
                break
            }
        }
    }
    return res
}
