class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = date.split('-')
        result = int(day)
        for i in range(1, int(month)):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                result += 31
            elif i in [4, 6, 9, 11]:
                result += 30
            elif i in [2]:
                if int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) % 100 != 0):
                    result += 29
                else:
                    result += 28
        return result
