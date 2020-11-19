class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = ""
        for ch in s:
            if 48 <= ord(ch) <= 57 or ch == '[':
                stack.append(ch)
            elif ch == ']':
                temp = ""
                while stack and stack[-1] != '[':
                    temp += stack.pop()
                # pop '['
                stack.pop()
                # pop number
                times = ""
                while stack and len(stack[-1]) == 1 and 48 <= ord(stack[-1]) <= 57:
                    times += (stack.pop())
                temp = temp[::-1] * int(times[::-1])
                if not stack:
                    result += temp
                else:
                    stack.append(temp[::-1])
            else:
                if not stack:
                    result += ch
                else:
                    stack.append(ch)
        return result
                
