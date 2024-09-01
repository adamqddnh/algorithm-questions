class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i in range(0, len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1
        return res
