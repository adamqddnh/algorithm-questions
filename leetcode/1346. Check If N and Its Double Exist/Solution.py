class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        setNumber = set(arr)
        for number in setNumber:
            if (number == 0):
                if (arr.count(0) > 1):
                    return True
                else:
                    continue
            if number + number in setNumber:
                return True
        return False
