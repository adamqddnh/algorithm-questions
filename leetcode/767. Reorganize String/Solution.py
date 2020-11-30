class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        threshold = (len(S) + 1) >> 1
        st = [0 for _ in range(0, 26)]
        maxCount = 0
        # 转化为字符出现频次结果集
        for s in S:
            temp = ord(s) - ord('a')
            st[temp] += 1
            maxCount = max(maxCount, st[temp])
        if maxCount > threshold:
            return ""
        # 结果集转换为元组
        tempCount = []
        for i in range(0, 26):
            if st[i] > 0:
                tempCount.append((chr(ord('a') + i), st[i]))
        # 倒序排序
        tempCount = sorted(tempCount, key = lambda x: x[1], reverse = True)

        tempResult = []
        result = []
        #将所有字符存放入一个数组中
        for tempSt, tempCount in tempCount:
            tempResult.extend(tempSt * tempCount)
            result.extend([None] * tempCount)

        result[::2], result[1::2] = tempResult[:(len(S) + 1) // 2], tempResult[(len(S) + 1) // 2:], 
        return ''.join(result)
