class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        position = [[_ if i == 1 else nums[_] for i in range(0, 2)] for _ in range(0, len(nums))]
        position.sort(key = lambda x: x[0])
        result = [0 for _ in range(0, len(nums))]
        for i in range(0, len(position)):
            pre = i
            while pre > 0 and position[pre][0] == position[pre - 1][0]:
                pre -= 1
            result[position[i][1]] = pre
        return result
