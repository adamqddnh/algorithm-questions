class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        minRecord = self.buildMinReocrd(nums)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > minRecord[i]:
                if not stack or stack[-1] > nums[i]:
                    stack.append(nums[i])
                else:
                    while stack and stack[-1] <= minRecord[i]:
                        stack.pop()
                    if stack and minRecord[i] < stack[-1] < nums[i]:
                        return True
                    
        return False
        
    def buildMinReocrd(self, nums):
        result = [0 for _ in range(0, len(nums))]
        minNum = nums[0]
        for i in range(0, len(nums)):
            minNum = min(minNum, nums[i])
            result[i] = minNum
        return result
