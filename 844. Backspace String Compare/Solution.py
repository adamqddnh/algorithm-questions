class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        pointer1, pointer2 = len(S) - 1, len(T) - 1
        flag = True
        while (pointer1 >= 0 or pointer2 >= 0) and flag:
            temp = 0
            flag = False

            while pointer1 >= 0 and ((S[pointer1] == "#") or temp > 0):
                if S[pointer1] == "#":
                    temp += 1
                else:
                    temp -= 1
                pointer1 -= 1
                flag = True
                
            temp = 0
            while pointer2 >= 0 and ((T[pointer2] == "#") or temp > 0):
                if T[pointer2] == "#":
                    temp += 1
                else:
                    temp -= 1
                pointer2 -= 1
                flag = True
                
            while pointer1 >= 0 and pointer2 >= 0 and S[pointer1] == T[pointer2] and S[pointer1] != "#":
                pointer1 -= 1
                pointer2 -= 1
                flag = True
                
        return True if pointer1 < 0 and pointer2 < 0 else False
