class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashSet.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        try:
            self.hashSet.remove(key)
        except:
            return

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashSet


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
