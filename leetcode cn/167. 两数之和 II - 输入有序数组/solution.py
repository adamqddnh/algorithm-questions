class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            sumNumber = numbers[left] + numbers[right]
            if sumNumber == target:
                break
            if sumNumber < target:
                left += 1
            else:
                right -= 1
            
        return [left+1, right+1]
