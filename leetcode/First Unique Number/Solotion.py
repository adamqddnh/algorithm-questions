class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numbers = []
        self.setA = set()
        self.setB = set()
        for number in nums:
            if number in self.setA:
                if number not in self.setB:
                    self.setB.add(number)
                    self.numbers.remove(number)
            else:
                self.setA.add(number)
                self.numbers.append(number)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if len(self.numbers) <= 0:
            return -1
        else:
            return self.numbers[0]

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.setA:
            if value not in self.setB:
                self.setB.add(value)
                self.numbers.remove(value)
        else:
            self.setA.add(value)
            self.numbers.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
