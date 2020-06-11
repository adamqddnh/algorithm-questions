class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numberArr = [0 for i in range(3)]
        currentNum = 0
        for i in range(0, len(nums)):
            numberArr[nums[i]] += 1
        tempNums = []
        for i in range(3):
            tempNums += [i] * numberArr[i]
        for i in range(0, len(tempNums)):
            nums[i] = tempNums[i]
