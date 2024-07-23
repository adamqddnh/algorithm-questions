package main
// import "fmt"

/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 
 * @param input int整型一维数组 
 * @param k int整型 
 * @return int整型一维数组
*/
func GetLeastNumbers_Solution( input []int ,  k int ) []int {
    if len(input) == 0 || k <= 0 {
        return []int{}
    }
    
    // write code here
    heap := buildHeap(input[:k], k)
    for i := k; i < len(input); i++ {
        if input[i] < heap[0] {
            heap[0] = input[i]
            heap = adjustHeap(heap, 0)
        }
    }
    return heap
}

func buildHeap(input []int, k int) []int {
    var (
        heap = input
    )
    for i := k / 2; i >= 0; i-- {
        heap = adjustHeap(heap, i)
    }
    
    return heap
}

func adjustHeap(heap []int, pos int) []int {
    var (
        length = len(heap)
    )
    for {
        child := pos + pos + 1
        if child >= length {
            break
        }
        if child + 1 < length && heap[child] < heap[child+1] {
            child++
        }
        if heap[pos] < heap[child] {
            heap[pos], heap[child] = heap[child], heap[pos]
            pos = child
        } else {
            break
        }
    }
    return heap
}
