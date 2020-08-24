class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        # Build a reverse trie tree
        self.root = {}
        self.stream = deque([])
        
        for word in set(words):
            currentRoot = self.root
            for s in word[::-1]:
                if s not in currentRoot:
                    currentRoot[s] = {}
                currentRoot = currentRoot[s]
            currentRoot['#'] = 1

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.appendleft(letter)
        return self.search(self.stream)
    
    def search(self, letters):
        currentNode = self.root
        for letter in letters:
            if letter not in currentNode:
                return False
            if '#' in currentNode[letter]:
                return True
            currentNode = currentNode[letter]
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
