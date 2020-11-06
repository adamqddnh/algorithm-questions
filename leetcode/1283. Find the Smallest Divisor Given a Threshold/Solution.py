class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left, right = 1, nums[-1]
        while left < right:
            mid = (left + right) / 2
            temp = 0
            for number in nums:
                temp += math.ceil((number + 0.0) / mid)
            if temp > threshold:
                left = mid + 1
            else:
                right = mid
        return left
