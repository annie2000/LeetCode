class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1 = len(s1)
        dictS1 = defaultdict(int)
        dictS2 = defaultdict(int)
        
        for ch in s1:
            dictS1[ch] += 1
        
        for i in range(len(s2)):
            dictS2[s2[i]] += 1
            
            if i >= lenS1:
                dictS2[s2[i-lenS1]] -= 1
                if(dictS2[s2[i-lenS1]] == 0):
                    del dictS2[s2[i-lenS1]]
            if dictS1 == dictS2:
                return True
            
        return False
                    
                
                
                
        
        