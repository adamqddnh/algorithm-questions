class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        real = [[cost[0]-cost[1], cost] for cost in costs]
        real.sort(key = (lambda x : x[0]))
        result = 0
        mid = len(real) / 2
        for i in range(0, len(real)):
            result = result + real[i][1][0] if i < mid else result + real[i][1][1]
        return result
