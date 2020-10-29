class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        start, end = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] - end == 1:
                end = nums[i]
            else:
                result.append(str(start) if start == end else "{}->{}".format(start, end))
                start, end = nums[i], nums[i]
                
        result.append(str(start) if start == end else "{}->{}".format(start, end))
 
        return result
