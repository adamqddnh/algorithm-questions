class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, left = {}, 0, -1
        for i in range(0, len(s)):
            if s[i] in dic:
                left = max(left, dic[s[i]])
            dic[s[i]] = i
            res = max(res, i - left)

        return res
