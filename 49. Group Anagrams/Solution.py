class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in result.keys():
                result[key].append(word)
            else:
                result[key] = [word]

                
        ret = []
        for oneResult in result:
            ret.append(result[oneResult])
        return ret
