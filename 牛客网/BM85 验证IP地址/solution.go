package main

import (
	"strconv"
	"strings"
)

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 验证IP地址
 * @param IP string字符串 一个IP地址字符串
 * @return string字符串
 */
func solve( IP string ) string {
    if isValidIPV4(IP) {
        return "IPv4"
    } else if isValidIPV6(IP) {
        return "IPv6"
    }
    return "Neither"
}

func isValidIPV4(ip string) bool {
    var ipArr = strings.Split(ip, ".")
    if len(ipArr) != 4 {
        return false
    }
    for _, num := range ipArr {
        if len(num) > 0 && num[0] == '0' {
            return false
        }
        x, err := strconv.Atoi(num) 
        if err != nil || x < 0 || x > 255 {
            return false
        }
    }
    return true
}

func isValidIPV6(ip string) bool {
    var ipArr = strings.Split(ip, ":")
    if len(ipArr) != 8 {
        return false
    }
    for _, num := range ipArr {
        if len(num) == 0 || len(num) > 4 {
            return false
        }
        _, err := strconv.ParseInt(num, 16, 32) 
        if err != nil {
            return false
        }
    }

    return true
}
