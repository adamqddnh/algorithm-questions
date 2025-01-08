func countPrefixSuffixPairs(words []string) int {
    var (
        res = 0
        length = len(words)
    )
    for i := 0; i < length - 1; i++ {
        for j := i+1; j < length; j++ {
            if isPrefixAndSuffix(words[i], words[j]) {
                res += 1
            }
        }
    }
    return res
}

func isPrefixAndSuffix(str1, str2 string) bool {
    var (
        len1 = len(str1)
        len2 = len(str2)
    )
    return len1 <= len2 && str1 == str2[:len1] && str1 == str2[len2-len1:]
}
