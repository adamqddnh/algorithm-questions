class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        numbers = [0] * 26
        for c in set(s):
            numbers[ord(c) - ord('a')] = s.count(c)
        stackSet = set()
        result = []

        for eachS in s:
            if eachS not in stackSet:
                while result and ord(result[-1]) > ord(eachS) and numbers[ord(result[-1]) - ord('a')] > 0:
                    temp = result.pop()
                    stackSet.remove(temp)
                result.append(eachS)
                stackSet.add(eachS)
            numbers[ord(eachS) - ord('a')] -= 1
        return ''.join(result)
