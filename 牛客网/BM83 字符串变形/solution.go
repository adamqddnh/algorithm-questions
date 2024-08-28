package main

import (
	"strings"
)

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 *
 * @param s string字符串
 * @param n int整型
 * @return string字符串
 */
func trans( s string ,  n int ) string {
    const diff = 'a' - 'A'
    var newStringBuffer = []byte(s)
    for i := range newStringBuffer {
        if 'a' <= newStringBuffer[i] && newStringBuffer[i] <= 'z' {
            newStringBuffer[i] -= diff
        } else if 'A' <= newStringBuffer[i] && newStringBuffer[i] <= 'Z' {
            newStringBuffer[i] += diff
        } else {
            continue
        }
    }
    res := strings.Split(string(newStringBuffer), " ")
    for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
        res[i], res[j] = res[j], res[i]
    }
    return strings.Join(res, " ")
}
