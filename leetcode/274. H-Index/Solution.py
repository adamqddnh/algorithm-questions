class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True);
        result = 0
        for i in range(0, len(citations)):
            if citations[i] >= i+1:
                result += 1
            else:
                break
        return result
