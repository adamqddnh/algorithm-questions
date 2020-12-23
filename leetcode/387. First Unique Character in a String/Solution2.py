class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charDict = collections.defaultdict(int)
        queue = []
        for i in range(0, len(s)):
            charDict[s[i]] += 1
            if charDict[s[i]] == 1:
                queue.append((s[i], i))

        for eachChar in queue:
            if charDict[eachChar[0]] == 1:
                return eachChar[1]

        return -1
