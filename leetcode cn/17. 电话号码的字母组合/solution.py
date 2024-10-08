class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitDict = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        res = []
        def dfs(combination, leftDigits):
            if len(leftDigits) == 0:
                res.append(combination)
            else:
                for digit in digitDict[leftDigits[0]]:
                    dfs(combination+digit, leftDigits[1:])
        dfs("", digits)
        return res
