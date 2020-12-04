class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = collections.defaultdict(int)
        end = collections.defaultdict(int)
        for number in nums:
            count[number] += 1
        
        for number in nums:
            if count[number] == 0:
                continue
            elif end[number - 1] > 0:
                end[number - 1] -= 1
                end[number] += 1
                count[number] -= 1
            elif count[number] > 0 and count[number+1] > 0 and count[number+2] > 0:
                count[number] -= 1
                count[number + 1] -= 1
                count[number + 2] -= 1
                end[number + 2] += 1
            else:
                return False
        
        for number in count:
            if count[number] > 0:
                return False

        return True
