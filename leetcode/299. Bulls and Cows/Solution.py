class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        l = len(secret)
        i = 0
        bulls = 0
        cows = 0
        secretDict = collections.defaultdict(int)
        guessRes = []
        while i < l:
            temp = secret[i]
            if secret[i] == guess[i]:
                bulls += 1
                temp = "#"
            else:
                guessRes.append(guess[i])
            secretDict[temp] += 1
            i += 1
            
        for ch in guessRes:
            if secretDict[ch] > 0:
                secretDict[ch] -= 1
                cows += 1
        return "{}A{}B".format(bulls, cows)
