class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.permutation(1, n, k, [])
        return self.result
        
    def permutation(self, start, n, k, tempRes):
        if len(tempRes) == k:
            # Add result
            self.result.append(tempRes)
            return
        if len(tempRes) + (n - start + 1) < k or start > n:
            # Rest numbers are not enough
            return
        for i in range(start, n+1):
            self.permutation(i+1, n, k, tempRes + [i])
