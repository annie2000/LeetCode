class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydic = {}
        
       
        for word in strs:
            sorW = ''.join(sorted(word))
            if sorW not in mydic:
                mydic[sorW] = []
            mydic[sorW].append(word)
        res = list(mydic.values())
        return res

    
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         mydic = collections.defaultdict(list)
#         #{('a', 'e', 't'): ['eat', 'tea', 'ate'], ('a', 'n', 't'): ['tan', 'nat'], ('a', 'b', 't'): ['bat']})
        
        

#         for word in strs:
#             sor_word = ''.join(sorted(word)) 
#             mydic[sor_word].append(word)
        
#         print(mydic)
#         return mydic.values()
            
        

            
        
        
        
    
            
            
            
            
        