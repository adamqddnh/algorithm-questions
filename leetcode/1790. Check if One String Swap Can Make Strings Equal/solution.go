func areAlmostEqual(s1 string, s2 string) bool {
    var (
        diff1, diff2 = -1, -1
        diffCount = 0
    )
    if len(s1) != len(s2) {
        return false
    }
    
    for i := 0; i < len(s1); i++ {
        if s1[i] != s2[i] {
            diffCount += 1
            if diffCount > 2 { // more than 2 diff
                return false
            } else if diffCount == 1 {
                diff1 = i
            } else {
                diff2 = i
            }
        }
    }

    if diffCount == 0 {
        return true
    }
    if diffCount == 2 && s1[diff1] == s2[diff2] && s1[diff2] == s2[diff1] {
        return true
    }

    return false
}
