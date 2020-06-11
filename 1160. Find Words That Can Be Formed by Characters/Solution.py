class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result = 0
        charsArr = [0 for i in range(26)]
        for char in chars:
            charsArr[ord(char) - ord('a')] += 1
        for word in words:
            flag = True
            for character in word:
                if word.count(character) > charsArr[ord(character) - ord('a')]:
                    flag = False
                    break
            if flag:
                result += len(word)
        return result
