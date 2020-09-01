class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        self.allTimes = set()
        self.fullPermutation(A, "")
        return self.getMaxTime()
        
    def fullPermutation(self, numbers, tempRes):
        if len(tempRes) == 4:
            self.allTimes.add(tempRes)
        for i in range(0, len(numbers)):
            self.fullPermutation(numbers[0:i] + numbers[i+1:], tempRes + str(numbers[i]))
            
    def getMaxTime(self):
        maxRes = -1
        result = ""
        for time in self.allTimes:
            if not self.isValidTime(time):
                continue
            else:
                if (int(time[:2]) * 60 + int(time[2:])) > maxRes:
                    maxRes = int(time[:2]) * 60 + int(time[2:])
                    result = time[:2] + ":" + time[2:]
        return result
                
    def isValidTime(self, time):
        return int(time[:2]) < 24 and int(time[2:]) < 60
