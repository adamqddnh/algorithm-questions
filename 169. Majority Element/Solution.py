class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = 0
        result = None
        for number in nums:
            if result == None:
                result = number
                times = 1
            elif number == result:
                times += 1
            else:
                times -= 1
            if times == 0:
                result = None
        return result
