class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.item = combinations(characters, combinationLength)
        self.n = sum(1 for _ in combinations(characters, combinationLength))

    def next(self):
        """
        :rtype: str
        """
        self.n -= 1
        return ''.join(next(self.item))

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
