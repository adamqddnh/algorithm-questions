class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minNumber = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.minNumber) == 0:
            self.minNumber.append(x)
        else:
            self.minNumber.append(min(x, self.minNumber[-1]))

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            self.stack = self.stack[:-1]
        if len(self.minNumber) > 0:
            self.minNumber = self.minNumber[:-1]

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minNumber) > 0:
            return self.minNumber[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
