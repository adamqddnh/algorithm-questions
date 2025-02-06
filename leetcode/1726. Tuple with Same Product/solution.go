func tupleSameProduct(nums []int) int {
    var (
        mapMultiRes = make(map[int]int)
        res = 0
    )
    for i := 0; i < len(nums); i++ {
        for j := i+1; j < len(nums); j++ {
            mapMultiRes[nums[i]*nums[j]] += 1
        }
    }
    for _, multiRes := range mapMultiRes {
        res += (multiRes - 1) * multiRes * 4
    }

    return res
}
