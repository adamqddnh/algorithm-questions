class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        res = []
        left, right = 0, 0
        for i in range(1, len(nums)):
            if nums[i] - nums[right] == 1:
                right = i
            else:
                res.append(self.appendResult(nums[left], nums[right]))
                left, right = i, i
        res.append(self.appendResult(nums[left], nums[right]))

        return res

    def appendResult(self, leftNum, rightNum) -> str:
        res = ""
        if leftNum == rightNum:
            res = "{}".format(leftNum)
        else:
            res = "{}->{}".format(leftNum, rightNum)
        return res
