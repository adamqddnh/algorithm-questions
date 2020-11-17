class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        lengthA = len(A)
        start = 0
        end = lengthA
        # filter down
        while start + 1 < lengthA:
            if A[start] >= A[start + 1]:
                start += 1
            else:
                break
                
        if lengthA - start < 3:
            return 0
        
        temp = 1
        flag = False
        while start + 2 < lengthA:
            # up
            end = start
            while end + 1 < lengthA and A[end] < A[end + 1]:
                temp += 1
                end += 1
            # down
            if (end > start):
                while end + 1 < lengthA and A[end] > A[end + 1]:
                    temp += 1
                    end += 1
                    flag = True
                
            if start == end:
                start += 1
            else:
                result = max(result, temp)
                temp = 1
                start = end
                
        print result
        return 0 if not flag or result < 3 else result
