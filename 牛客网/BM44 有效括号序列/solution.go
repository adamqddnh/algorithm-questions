package main
// import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param s string字符串 
 * @return bool布尔型
*/
func isValid( s string ) bool {
    // write code here
    var mapValid = map[string]string{
        ")": "(",
        "]": "[",
        "}": "{",
    }
    var stack []string
    for _, st := range s {
        str := string(st)
        if str == "(" || str == "[" || str == "{" {
            stack = append(stack, str)
        } else if value, ok := mapValid[str]; ok {
            if len(stack) == 0 {
                return false
            }
            if stack[len(stack)-1] == value {
                stack = stack[:len(stack)-1]
            } else {
                return false
            }
        }
    }
    return len(stack) == 0
}
