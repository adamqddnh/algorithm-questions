class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n+1):
            temp = str(i)
            if i % 15 == 0:
                temp = "FizzBuzz"
            elif i % 5 == 0:
                temp = "Buzz"
            elif i % 3 == 0:
                temp = "Fizz"
            result.append(str(temp))
        return result
