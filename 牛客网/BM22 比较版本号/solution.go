package main

import (
	"fmt"
	"strconv"
	"strings"
)

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 比较版本号
 * @param version1 string字符串
 * @param version2 string字符串
 * @return int整型
 */
func compare( version1 string ,  version2 string ) int {
    // write code here
    version1Arr := strings.Split(version1, ".")
    version2Arr := strings.Split(version2, ".")
    l1, l2 := len(version1Arr), len(version2Arr)
    for i := 0; i < min(l1, l2); i++ {
        int1 := strToInt(version1Arr[i])
        int2 := strToInt(version2Arr[i])
        fmt.Println(i, int1, int2)
        if int1 < int2 {
            return -1
        } else if int1 > int2 {
            return 1
        }
    }

    if l1 < l2 {
        for i := l1; i < l2; i++ {
            if strToInt(version2Arr[i]) > 0 {
                return -1
            }
        }
    } else if l1 > l2 {
        for i := l2; i < l1; i++ {
            if strToInt(version1Arr[i]) > 0 {
                return 1
            }
        }
    }

    return 0
}

func min(int1 int, int2 int) int {
    if int1 < int2 {
        return int1
    }
    return int2
}

func strToInt(str string) int {
    res, _ := strconv.Atoi(str)
    return res
}
