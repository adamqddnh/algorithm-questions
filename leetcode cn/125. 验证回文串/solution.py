class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "".join(ch.lower() for ch in s if ch.isalnum())
        return newStr == newStr[::-1]
