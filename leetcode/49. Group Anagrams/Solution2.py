class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = collections.defaultdict(list)
        for eachStr in strs:
            key = ''.join(sorted(eachStr))
            result[key].append(eachStr)
        
        return list(result.values())
