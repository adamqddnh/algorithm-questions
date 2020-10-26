class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numberCounter, sortedCounter = [0 for i in range(101)], [0 for i in range(101)]
        for number in nums:
            numberCounter[number] += 1
        for i in range(1, len(numberCounter)):
            sortedCounter[i] = sortedCounter[i-1] + numberCounter[i-1]
        for i in range(0, len(nums)):
            nums[i] = sortedCounter[nums[i]]
        return nums
