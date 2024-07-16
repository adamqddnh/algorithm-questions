package main

var stack []int
var minStack []int

func Push(node int) {
    // write code here
    if len(stack) == 0 {
        minStack = append(minStack, node)
    } else {
        minStack = append(minStack, minInt(node, minStack[len(minStack) - 1]))
    }
    stack = append(stack, node)
}

func Pop() {
    // write code here
    if len(stack) == 0 {
        return
    }
    stack = stack[:len(stack)-1]
    minStack = minStack[:len(minStack)-1]
}

func Top() int {
    // write code here
    return stack[len(stack)-1]
}

func Min() int {
    // write code here
    return minStack[len(minStack)-1]
}

func minInt(a, b int) int {
    if a > b {
        return b
    }
    return a
}
