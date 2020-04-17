class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        last = 0
        result = 1
        length = len(arr)
        for i in range(1, length):
            if arr[i] == arr[last]:
                result = max(result, i - last + 1)
            else:
                last = i
            if result > length / 4:
                return arr[last]
        return arr[last]
    
    """
    :A new idea
    """
#     def findSpecialInteger(self, arr):
#         n = len(arr) // 4
#         for i in range(len(arr)):
#             if arr[i] == arr[i + n]:
#                 return arr[i]
