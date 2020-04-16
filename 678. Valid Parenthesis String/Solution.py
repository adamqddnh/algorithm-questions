class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        star = []
        for i in range(0, len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if len(left) > 0:
                    left.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
                
        if len(left) > len(star):
            return False
        
        while len(left) > 0:
            if left.pop() > star.pop():
                return False
            
        return True
