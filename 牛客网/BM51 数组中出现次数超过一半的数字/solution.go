package main
// import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param numbers int整型一维数组 
 * @return int整型
*/
func MoreThanHalfNum_Solution( numbers []int ) int {
    // write code here
    var num = -1
    var times = 0
    for _, number := range numbers {
        if num == number {
            times++
        } else {
            times--
            if times < 0 {
                num = number
                times = 1
            }
        }
    }
    return num
}
