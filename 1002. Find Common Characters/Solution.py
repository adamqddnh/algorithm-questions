class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        chrNum = [0 for i in range(0, 26)]
        for char in A[0]:
            chrNum[ord(char)-97] += 1
            
        temp = [0 for i in range(0, 26)]
        for i in range(1, len(A)):
            for char in A[i]:
                if chrNum[ord(char)-97] > 0:
                    chrNum[ord(char)-97] -= 1
                    temp[ord(char)-97] += 1
            chrNum = temp
            temp = [0 for i in range(0, 26)]
        
        result = []
        for i in range(0, len(chrNum)):
            if chrNum[i] > 0:
                for j in range(0, chrNum[i]):
                    result.append(chr(i+97))
                    
        return result
