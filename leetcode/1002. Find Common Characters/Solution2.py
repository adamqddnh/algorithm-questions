class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A:
            return []

        record = collections.defaultdict(int)
        for ch in A[0]:
            record[ch] += 1
        for i in range(1, len(A)):
            temp = collections.defaultdict(int)
            for ch in A[i]:
                if record[ch] > 0:
                    record[ch] -= 1
                    temp[ch] += 1
            record = temp
        result = []
        for key in record:
            if record[key] > 0:
                for i in range(record[key]):
                    result.append(key)
        return result
