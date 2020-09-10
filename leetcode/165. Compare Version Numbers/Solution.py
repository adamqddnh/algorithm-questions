class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versionArr1 = version1.split('.')
        versionArr2 = version2.split('.')
        l1 = len(versionArr1)
        l2 = len(versionArr2)
        for i in range(0, min(l1, l2)):
            if int(versionArr1[i]) < int(versionArr2[i]):
                return -1
            elif int(versionArr1[i]) > int(versionArr2[i]):
                return 1
            else:
                continue
        for j in range(i+1, max(l1, l2)):
            if j < l1 and int(versionArr1[j]) > 0:
                return 1
                
            if j < l2 and int(versionArr2[j]) > 0:
                return -1
                
        return 0
