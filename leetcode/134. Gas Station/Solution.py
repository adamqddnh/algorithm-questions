class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        spare = 0
        minPosition = 0
        minSpare = sys.maxint
        for i in range(0, len(cost)):
            spare += gas[i] - cost[i]
            if spare < minSpare:
                minSpare = spare
                minPosition = i
        return -1 if spare < 0 else (minPosition + 1) % len(gas)
