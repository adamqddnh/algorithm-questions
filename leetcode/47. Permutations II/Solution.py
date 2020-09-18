class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.record = set()
        self.result = []
        self.dfs(nums, [], len(nums))
        return self.result

    def dfs(self, nums, tempRes, n):
        if len(tempRes) == n:
            temp = ','.join([str(i) for i in tempRes])
            if temp not in self.record:
                self.record.add(temp)
                self.result.append(tempRes)
                return
        
        for i in range(0, len(nums)):
            self.dfs(nums[:i] + nums[i+1:], tempRes + [nums[i]], n)
