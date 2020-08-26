class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = [ _ for _ in dic.get(digits[0])]
        tempRes = result[:]
        for i in range(1, len(digits)):
            result = []
            for j in range(0, len(tempRes)):
                for _ in dic.get(digits[i]):
                    result.append(tempRes[j] + _)
            tempRes = result[:]
        return result
