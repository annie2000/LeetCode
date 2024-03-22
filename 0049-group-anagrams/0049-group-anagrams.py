class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydic = collections.defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            mydic[key].append(word)
        
        return mydic.values()
        