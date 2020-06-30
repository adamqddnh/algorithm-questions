class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numberSum = 0
        result = 0
        sumDict = collections.defaultdict(int)
        sumDict[0] = 1
        for i in range(0, len(nums)):
            numberSum += nums[i]
            if (numberSum - k) in sumDict:
                result += sumDict[numberSum - k]
            sumDict[numberSum] += 1
            
        return result
