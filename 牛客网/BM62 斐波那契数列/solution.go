package main

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param n int整型 
 * @return int整型
*/
func Fibonacci( n int ) int {
    if n == 1 || n == 2 {
        return 1
    }

    return Fibonacci(n-1) + Fibonacci(n-2)
}
