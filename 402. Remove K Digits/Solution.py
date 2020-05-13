class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = ""
        for char in num:
            if result == "":
                result += char
            else:
                while len(result) > 0 and result[-1] > char and k > 0:
                    result = result[:-1]
                    k -= 1
                result += char
                
        while k > 0:
            result = result[:-1]
            k -= 1
        
        while result != "" and result[0] == "0":
            result = result[1:]
        
        return result if result != "" else "0"
