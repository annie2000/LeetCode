class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        tdic={}
        
        for c in s:
            if c not in sdic:
                sdic[c] = 1
            sdic[c] +=1
        
        for c in t:
            if c not in tdic:
                tdic[c] = 1
            tdic[c] +=1
        
        if sdic != tdic:
            return False
        return True
        
        
        