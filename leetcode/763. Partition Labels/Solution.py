class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {ch: i for i, ch in enumerate(S)}
        result = []
        start = 0
        end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ch])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result
