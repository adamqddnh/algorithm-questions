class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trustArrA = [[0 for i in range(0, N+1)] for j in range(0, N+1)]
        trustArrB = [[0 for i in range(0, N+1)] for j in range(0, N+1)]
        
        for eachTrust in trust:
            trustArrA[eachTrust[1]][eachTrust[0]] = 1
            trustArrB[eachTrust[0]][eachTrust[1]] = 1
            
        for i in range(1, len(trustArrA)):
            if (sum(trustArrA[i]) >= N-1):
                if (sum(trustArrB[i]) == 0):
                    return i
        
        return -1
