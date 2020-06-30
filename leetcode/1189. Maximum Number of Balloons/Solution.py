class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        charDict = collections.defaultdict(int)
        for char in text:
            charDict[char] += 1
        return min(charDict['b'], charDict['a'], charDict['l'] / 2, charDict['o'] / 2, charDict['n'])
