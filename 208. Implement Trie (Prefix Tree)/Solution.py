class Node():
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isLeaf = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root
        for eachWord in word:
            current = current.children[eachWord]
        current.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for eachWord in word:
            if not current.children.get(eachWord):
                return False
            current = current.children[eachWord]
        return current.isLeaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for pre in prefix:
            if not current.children.get(pre):
                return False
            current = current.children[pre]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
