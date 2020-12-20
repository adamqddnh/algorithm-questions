class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        totalSize = 0
        for s in S:
            if ord('0') <= ord(s) <= ord('9'):
                totalSize *= int(s)
            else:
                totalSize += 1
            if totalSize >= K:
                break
            
        for s in S[::-1]:
            K %= totalSize
            if K == 0 and s.isalpha():
                return s
            
            if ord('0') <= ord(s) <= ord('9'):
                totalSize /= int(s)
            else:
                totalSize -= 1
                
        return None
