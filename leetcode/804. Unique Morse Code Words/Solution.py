class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = collections.defaultdict(int)
        
        for word in words:
            temp = ""
            for s in word:
                temp += morseCode[ord(s) - 97]
            result[temp] += 1
        
        return len(result)
