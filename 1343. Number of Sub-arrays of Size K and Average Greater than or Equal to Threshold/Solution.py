class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        result = 0
        sumNumber = sum(arr[:k-1])
        for i in range(k-1, len(arr)):
            sumNumber += arr[i]
            if sumNumber / k >= threshold:
                result += 1
            sumNumber -= arr[i-k+1]
        return result
