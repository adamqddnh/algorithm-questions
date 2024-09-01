class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        res = length+1
        left, right = 0, 0
        sumNumber = 0
        while right < length:
            sumNumber += nums[right]
            while sumNumber >= target:
                res = min(res, right-left+1)
                if res == 1:
                    break
                sumNumber -= nums[left]
                left += 1
            right += 1
        
        return res if res <= length else 0
            
