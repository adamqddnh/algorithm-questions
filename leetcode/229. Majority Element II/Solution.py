class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b, countA, countB = 0, 0, 0, 0
        for number in nums:
            if a == number:
                countA += 1
                continue
            if b == number:
                countB += 1
                continue
            if countA == 0:
                a = number
                countA = 1
                continue
            if countB == 0:
                b = number
                countB = 1
                continue
            countA -= 1
            countB -= 1
            
        countA = 0
        countB = 0
        for number in nums:
            if number == a:
                countA += 1
            elif number == b:
                countB += 1
                
        result = []
        if countA > len(nums) / 3:
            result.append(a)
        if countB > len(nums) / 3:
            result.append(b)
            
        return result
