class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0
        positionMap = {}
        positionMap[0] = -1
        temp = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                temp -= 1
            if temp in positionMap:
                result = max(result, i - positionMap[temp])
            else:
                positionMap[temp] = i
        
        return result
