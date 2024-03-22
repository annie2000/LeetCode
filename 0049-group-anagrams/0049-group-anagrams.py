
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydic = {}
        # res = []
       
        for word in strs:
            sorW = ''.join(sorted(word))
            if sorW not in mydic:
                mydic[sorW] = []
            mydic[sorW].append(word)
        res = list(mydic.values())
        return res
        
        

            
        
        
        
    
            
            
            
            
        