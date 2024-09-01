class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if len(stack) == 0 or stack[-1] != dic[i]:
                    return False
                stack = stack[:-1]
        
        return len(stack) == 0
