package main

var arr []int

func Insert(num int){
	var (
        left = 0
        right = len(arr) - 1
    )
    for left <= right {
        mid := (left + right) / 2
        if arr[mid] == num {
            arr = append(arr[:mid], append([]int{num}, arr[mid:]...)...)
            return
        } else if arr[mid] > num {
            right = mid - 1
        } else if arr[mid] < num {
            left = mid + 1
        }
    }
    arr = append(arr[:left], append([]int{num}, arr[left:]...)...)
}

func GetMedian() float64{
    var (
        res = 0.0
        length = len(arr)
    )
    if length == 0 {
        return res
    }

    if length % 2 == 1 {
        res = float64(arr[length / 2])
    } else {
        res = float64(arr[length / 2] + arr[length / 2 - 1]) / 2
    }

	return res
}
