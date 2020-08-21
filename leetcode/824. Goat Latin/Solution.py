class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        end = "ma"
        result = ""
        for word in S.split():
            end += "a"
            if word[0] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
                result += word + end + " "
            else:
                result += word[1:] + word[0] + end + " "
            
        return result.strip()
