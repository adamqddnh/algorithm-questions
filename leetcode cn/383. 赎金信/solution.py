class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict, magazineDict = defaultdict(int), defaultdict(int)
        for i in range(0, len(ransomNote)):
            ransomNoteDict[ransomNote[i]] += 1
        for i in range(0, len(magazine)):
            magazineDict[magazine[i]] += 1
        for key in ransomNoteDict.keys():
            if ransomNoteDict[key] > magazineDict[key]:
                return False

        return True
