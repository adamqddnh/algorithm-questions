class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        temperatureStack = []
        result = [0 for i in range(0, len(T))]
        for i in range(0, len(T)):
            if len(temperatureStack) == 0:
                temperatureStack.append(i)
            else:
                while len(temperatureStack) > 0 and T[temperatureStack[-1]] < T[i]:
                    result[temperatureStack[-1]] = i - temperatureStack[-1]
                    temperatureStack.pop()
                temperatureStack.append(i)
        return result
